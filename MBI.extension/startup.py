# Imports
# ------------------------------------------------------------------------------
import subprocess

# Variables
# ------------------------------------------------------------------------------
if versie_server != versie_user:
    batpath = r"C:\Users\AlexanderV\OneDrive - b-b.be\Bureaublad\PlotFolder\04_Werkfolder\00_THOMAS MORE\24_MasterBuildingIntelligence\UI\Github\Master-Building-Intelligence\MBI.extension\bin\Update\update.bat"

    try:
        # Run the batch file
        process = subprocess.Popen(["start", "cmd", "/k", batpath], shell=True)
        process.wait()
    except Exception as e:
        print("An error occurred while running the batch file: {}".format(e))












# try:
#     output.freeze()
#     process = subprocess.Popen(["start", "cmd", "/k", file_path], shell=True)
#     process.wait()
#     output.unfreeze()
#     return True
# except Exception as e:
#     print("An error occurred while running the batch file: {}".format(e))
#     return False