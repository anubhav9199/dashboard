from Lib.utils import title_awesome
from core.file_upload import FileUploadEngine

def write():
    title_awesome('File Upload')
    FileUploadEngine.file_upload_main(
        'File Upload', 'Upload data file here....!!!')
