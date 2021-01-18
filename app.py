from flask import Flask, render_template, request
from stories import *

app = Flask(__name__)

@app.route("/madlib")
def get_prompts():
    prompts = story.prompts
    return render_template("mad_lib.html", prompts=prompts)

@app.route("/story")
def create_story():
    answers = {f"{prompt}": request.args.get(f"{prompt}") for prompt in story.prompts}
    story_text = story.generate(answers)
    return render_template("story.html", story=story_text)


