##original repo https://huggingface.co/stabilityai/sdxl-turbo
##import

from diffusers import AutoPipelineForText2Image
import torch
import time

def gen(prompt): ##func on generation image
    ##load model stabilityai/sdxl-turbo
    pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo",
                                                     torch_dtype=torch.float16,
                                                     variant="fp16")
    ##cpu or cuda
    pipe.to("cuda")
    ##gen image
    image = pipe(prompt=prompt,
                 num_inference_steps=1,
                 guidance_scale=0.0).images[0]
    image.save(f"static/{prompt}.png") ## save image
    time.sleep(0.5)