import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

supresh_image = face_recognition.load_image_file("supresh.jpg")
supresh_face_encoding = face_recognition.face_encodings(supresh_image)[0]

known_face_encodings = [
    supresh_face_encoding
]
known_face_names = [
    "Supresh"
]

faces = []
while True:
	ret, frame = video_capture.read()
	rgb_frame = frame[:, :, ::-1]
	
	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
	
	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
		name = "Unknown"
		if True in matches:
			first_match_index = matches.index(True)
			name = known_face_names[first_match_index]
			faces.append(name)
		
		cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0,0,255), cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, name, (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)
	cv2.imshow('Video', frame)
	
	print(faces)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
video_capture.release()
cv2.destroyAllWindows()
