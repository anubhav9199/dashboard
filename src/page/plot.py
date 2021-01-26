from Lib.utils import title_awesome
from core.file_upload import FileUploadEngine

def write():
    title_awesome('Plots & Graphs')
    FileUploadEngine.file_upload_main(
        'Plots & Graphs', 'Plotting data you gave.')
