from operator import itemgetter
from mmaction.apis import init_recognizer, inference_recognizer

config_file = {"Config_file_location"}
checkpoint_file = {"Checkpoint_file_location"}
video_file = r"C:\Users\Sid1t\Downloads\WhatsApp Video 2024-01-24 at 10.45.37 PM.mp4"
model = init_recognizer(config_file, checkpoint_file)  # or device='cuda:0'
pred_result = inference_recognizer(model, video_file)
#%%
print(pred_result)
# %%
