"""
Build the documentation using pdoc (not pdoc3)
"""
import shutil
import glob
import os


PKG_NAME = 'pyosv'
# Clean documentation folder
shutil.rmtree('./docs/', ignore_errors=True)

os.mkdir("./docs/")
os.mkdir(f"./docs/{PKG_NAME}/")

# Build documentation
os.system(f"pdoc ./{PKG_NAME} -o ./docs --docformat numpy --logo ./logo.png -t ./docs_assets/") #--logo https://casperfibaek.github.io/buteo/logo.png --favicon https://casperfibaek.github.io/buteo/favicon.ico

shutil.copy2("./docs_assets/logo.png", "./docs/logo.png")
shutil.copy2(f"./docs_assets/logo.png", f"./docs/{PKG_NAME}/logo.png")

for p in glob.glob(f"./docs/{PKG_NAME}/*/"):
    shutil.copy2("./docs_assets/logo.png", p+"/logo.png")

