#!/usr/bin/python
from pixai import PixaiAPI
import io
import os
import sys
import time
from PIL import Image
from credentials import *


# model url looks like pixai.art/model/12345/67890
# use the second number which refers to the specific version of a model
# model = 1632080534138643945 # epic realism

# the following is a good preset that I recommend
model = 1693971202393705839 # western toon style
lora = {
    '1613982114424770324': 0.7, # western illustration vector
    '1638766839267720162': 0.5, # niji-flat
}
# the following will be added to all prompts
preamble = "mugshot, western illustration, clean lines, minimalist, "

# whether to use high priority tasks, which cost more credits
high_priority = False

def main():
    client = PixaiAPI(token)
    argv = sys.argv
    if len(argv) == 3:
        filename = argv[1]
        task = client.img2img(filename, preamble + argv[2],
                              size=(480, 576),
                              priority=1000 if high_priority else 0,
                              modelId=model,
                              lora=lora,
                              strength=0.6,
                              steps=14,
                              batchSize=4,
                              )
        while True:
            if task.get_data():
                image = Image.open(io.BytesIO(task.data)).crop((0, 0, 480, 576))
                # you can further process the image here
                # for example, make the background transparent
                # image = rembg.remove(image)
                image.save(filename+".tmp.png")
                os.replace(filename+".tmp.png", filename) # save then rename to avoid partially-written files
                break
            else:
                time.sleep(1)

if __name__ == "__main__":
    main()
