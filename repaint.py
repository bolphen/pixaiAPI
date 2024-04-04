#!/usr/bin/python
from pixai import PixaiAPI
import io
import os
import sys
import time
from PIL import Image

# this is a throwaway account
# please replace this with your own token
token = "eyJhbGciOiJFUzUxMiIsInR5cCI6IkpXVCJ9.eyJsZ2EiOjE3MTIyMTEyMzIsImlhdCI6MTcxMjIxMTI1MCwiZXhwIjoxNzEyODE2MDUwLCJpc3MiOiJwaXhhaSIsInN1YiI6IjE3MzI1MDY4MjQyNjUxMTc3MjIiLCJqdGkiOiIxNzMyNTA2ODI0NzI2NDkxMTY3In0.AK2kUNXq3OFrRbrewThx5a80O2LUgx223hmG3wy_Yg7bFl9YJxZ2kTJFSG0ilXSwPbDgrZV4lsjuVvpG3odiEaD6AdsZGm2dLXIjxYc_NNbJ4sCRB6l_dVFCm4D9ja1ppMi4Z5ZW0Qze66Byf8MqyoC_ykfIATUNfUfdvJicL71CoRB5"

# model url looks like pixai.art/model/12345/67890
# use the second number which refers to the specific version of a model
model = 1647780283914444571

# whether to use high priority tasks, which cost more credits
high_priority = False

def main():
    client = PixaiAPI(token)
    argv = sys.argv
    if len(argv) == 3:
        filename = argv[1]
        task = client.img2img(filename, argv[2],
                              size=(480, 576),
                              priority=1000 if high_priority else 0,
                              modelId=model)
        while True:
            if task.get_data():
                image = Image.open(io.BytesIO(task.data))
                # you can further process the image here
                # for example, make the background transparent
                image.save(filename+".tmp.png")
                os.rename(filename+".tmp.png", filename) # save then rename to avoid partially-written files
                break
            else:
                time.sleep(1)

if __name__ == "__main__":
    main()
