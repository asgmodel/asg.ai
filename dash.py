import gradio as gr
import sys


from ASGAPI import ASGModels

ASGAI=ASGModels.ASG(isForm=False)
choices=[
          "Group",
          "Technique",
          "Software"
                              ]
model_choices = gr.Dropdown(
                            choices=choices,
                            label="اختر النموذج",
                            value="Group",
                        )



import gradio as gr
def home_page():
    return """
    <div class="px-4 py-5 my-5 text-center">
    <img class="d-block mx-auto mb-4" src="/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57">
    <h1 class="display-5 fw-bold">مرحباً بك في Model AI ASG
 </h1>
    <div class="col-lg-6 mx-auto">
      <p class="lead mb-4">
      Wasm-Speeker We provide models that help to aid in the creation of different attack sequences. You can deal with AGS models by choosing the model you want. We provide models that help to aid in the creation of different attack sequences. You can deal with AGS models by choosing the model you want.      </p>
      <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
        <button type="button" class="btn btn-primary btn-lg px-4 gap-3">Primary button</button>
        <button type="button" class="btn btn-outline-secondary btn-lg px-4">Secondary</button>
      </div>
    </div>
  </div>
  
    <div class="container col-xxl-8 px-4 py-5">
    <div class="row flex-lg-row-reverse align-items-center g-5 py-5">
      <div class="col-10 col-sm-8 col-lg-6">
        <img src="bootstrap-themes.png" class="d-block mx-lg-auto img-fluid" alt="Bootstrap Themes" width="700" height="500" loading="lazy">
      </div>
      <div class="col-lg-6">
        <h1 class="display-5 fw-bold lh-1 mb-3">Responsive left-aligned hero with image</h1>
        <p class="lead">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
        <div class="d-grid gap-2 d-md-flex justify-content-md-start">
          <button type="button" class="btn btn-primary btn-lg px-4 me-md-2">Primary</button>
          <button type="button" class="btn btn-outline-secondary btn-lg px-4">Default</button>
        </div>
      </div>
    </div>
  </div>
  <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
      <div class="col-lg-7 p-3 p-lg-5 pt-lg-3">
        <h1 class="display-4 fw-bold lh-1">Border hero with cropped image and shadows</h1>
        <p class="lead">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
        <div class="d-grid gap-2 d-md-flex justify-content-md-start mb-4 mb-lg-3">
          <button type="button" class="btn btn-primary btn-lg px-4 me-md-2 fw-bold">Primary</button>
          <button type="button" class="btn btn-outline-secondary btn-lg px-4">Default</button>
        </div>
      </div>
      <div class="col-lg-4 offset-lg-1 p-0 overflow-hidden shadow-lg">
          <img class="rounded-lg-3" src="bootstrap-docs.png" alt="" width="720">
      </div>
    </div>
   <div class="bg-dark text-secondary px-4 py-5 text-center">
    <div >
      <h1 class="display-5 fw-bold text-white">Dark mode hero</h1>
      <div class="col-lg-6 mx-auto">
        <p class="fs-5 mb-4">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <button type="button" class="btn btn-outline-info btn-lg px-4 me-sm-3 fw-bold">Custom button</button>
          <button type="button" class="btn btn-outline-light btn-lg px-4">Secondary</button>
        </div>
      </div>
    </div>
  </div>
    """
def t2t(text, namn_model):
    if namn_model == "Group":
        out = ASGAI.Group.predictAPI(text)
    elif namn_model == "Technique":
        out = ASGAI.Tec.predictAPI(text)
    else:
        out = ASGAI.Soft.predictAPI(text)
    return str(out)

def t2seq(text, namn_model):
    if namn_model == "Group":
        out = ASGAI.Group.Predict_ALL(text)
    elif namn_model == "Technique":
        out = ASGAI.Tec.Predict_ALL(text)
    else:
        out = ASGAI.Soft.Predict_ALL(text)
    return str(out)
def echo(message, history):
    text=t2seq(message,"Group")
    return text


# Use Blocks
with gr.Blocks() as demo:
    gr.HTML("""
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <title> Model AI ASG</title>
    </head>
    """)

    # العنوان الرئيسي
    gr.Markdown("# Model AI ASG")
    

    # عرض الصورة الترحيبية
    gr.HTML("""
    <style>
    .gradio-tabs {
        direction: rtl;
    }
    </style>
    """)
    
    with gr.Row():
        with gr.Tab("Home"):
            gr.HTML(home_page())
        with gr.Tab("Thread Base"):
            gr.Markdown("### Thread Base")
            with gr.Row():
           
                with gr.Tab("T2T"):
                        text_input = gr.Textbox(label="Input Text")
                        model_choices = gr.Dropdown(choices=["Group", "Technique", "Soft"], label="Model",value="Group",)
                        text_output = gr.Textbox(label="Output")
                        submit_btn = gr.Button("Submit")
                        submit_btn.click(fn=t2t, inputs=[text_input, model_choices], outputs=text_output)
                    
                with gr.Tab("T2Seq"):
                        text_input_seq = gr.Textbox(label="Input Text")
                        model_choices_seq = gr.Dropdown(choices=["Group", "Technique", "Soft"], label="Model",value="Group",)
                        text_output_seq = gr.Textbox(label="Output")
                        submit_btn_seq = gr.Button("Submit")
                        submit_btn_seq.click(fn=t2seq, inputs=[text_input_seq, model_choices_seq], outputs=text_output_seq)

                with gr.Tab("T2Sinaro"):
                    model_choices_seq1 = gr.Dropdown(choices=["Group", "Technique", "Soft"], label="Model",value="Group",)
                    gr.ChatInterface(fn=echo, examples=["hello", "hola", "merhaba"], title="Echo Bot")
                    
                    

                    
        with gr.Tab("Stute Base"):
                gr.Markdown("### Stute Base")

