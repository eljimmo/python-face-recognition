import face_recognition 

image = face_recognition.load_image_file('biden.jpeg')
face_location = face_recognition.face_locations(image)

#array of coords of each face
print(face_location)

