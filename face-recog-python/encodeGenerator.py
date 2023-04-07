import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sbhfaceidhospital-default-rtdb.firebaseio.com/",
    'storageBucket': "sbhfaceidhospital.appspot.com"
})

# importing the face images into a list
# folderPath = 'Images'
# pathList = os.listdir(folderPath)
# imgList = []
# iDs = []
# for path in pathList:
#     imgList.append(cv2.imread(os.path.join(folderPath, path)))
#     iDs.append(os.path.splitext(path)[0])

    # fileName = f'{folderPath}/{path}'
    # bucket = storage.bucket()
    # blob = bucket.blob(fileName)
    # blob.upload_from_filename(fileName)
# print(len(imgList))


def findencodings():
    folderPath = 'Images'
    pathList = os.listdir(folderPath)
    imgList = []
    iDs = []
    for path in pathList:
        imgList.append(cv2.imread(os.path.join(folderPath, path)))
        iDs.append(os.path.splitext(path)[0])
    encodelist = []
    for img in imgList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)

    encodedListKnownWithIds = [encodelist, iDs]
    file = open('encodeFile.p', 'wb')
    pickle.dump(encodedListKnownWithIds, file)
    file.close()
    print('File Saved')
    # return [encodelist, iDs]


# print('Encoding started...')
# # encodedListKnownWithIds = findencodings()
# # encodedListKnownWithIds = [encodedListKnown, iDs]
# print('Encoding finished')

# file = open('encodeFile.p', 'wb')
# pickle.dump(encodedListKnownWithIds, file)
# file.close()
# print('File Saved')


# def addencoding(idtodownload):
#     bucketd = storage.bucket()
#     for idval in range(1, idtodownload+1):
#         source_blob_name = f'{folderPath}/{idval}.jpg'
#         blobd = bucketd.get_blob(source_blob_name)
#         downloadpath = r"img.jpg"
#         blobd.download_to_filename(downloadpath)
#         img2 = cv2.imread(downloadpath)
#         img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img2)[0]
#         encodedwithid = [encode, idtodownload]
#     # file2 = open('encodeFile.p', 'ab')
#     # pickle.dump(encodedwithid, file2)
#     # file2.close()
#     # os.remove(downloadpath)
#     print('encoding added of last image')

def addimage(imageid):
    bucket = storage.bucket()
    source_blob_name = f'Images/{imageid}.jpg'
    blob = bucket.get_blob(source_blob_name)
    downloadpath = source_blob_name
    blob.download_to_filename(downloadpath)
    findencodings()

# addencoding(8)

addimage(8)
