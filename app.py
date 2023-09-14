import gradio as gr
import tensorflow as tf
import cv2

title = "CoviDigiScan"

head = (
  "<center>"
  "Upload an X-ray image to check for covid19"
  "</center>"
)


cnn = tf.keras.models.load_model("cnn_model.h5")

def predict_input_image(img):
    img = img.reshape(1, 500, 500, 1)
    prediction = cnn.predict(img).tolist()[0]
    class_names = ["Covid"]
    if preds[i, 0] >= 0.5: 
        return {class_names[i]: prediction[i] for i in range(1)}
    else:  
        return {class_names[i]: 1-prediction[i] for i in range(1)}

image = gr.inputs.Image(shape=(500, 500), image_mode='L', invert_colors=False, source="upload")
label = gr.outputs.Label()
iface = gr.Interface(fn=predict_input_image, inputs=image, outputs=label,title=title, description=head)
iface.launch()
