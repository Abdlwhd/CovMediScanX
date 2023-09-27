import gradio as gr
import tensorflow as tf
import cv2

title = "CovMediScanX"

head = (
  "<center>"
  "Upload an X-ray image to check for covid19"
  "</center>"
)


cnn = tf.keras.models.load_model("cnn_model.h5")

def predict_input_image(img):
    img = img.reshape(1, 299, 299, 1)
    prediction = cnn.predict(img)
    prediction[prediction <= 0.5] = 0
    prediction[prediction > 0.5] = 1
    if prediction == 0:
        return "Normal"
    elif prediction== 1:
        return "Covid"

image = gr.inputs.Image(shape=(299, 299), image_mode='L', invert_colors=False, source="upload")
label = gr.outputs.Label()
iface = gr.Interface(fn=predict_input_image, inputs=image, outputs=label,title=title, description=head)
iface.launch()
