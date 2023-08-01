import os
from flask import Flask, request, jsonify
from llama import Llama
from transformers import AutoTokenizer
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

Llama_dir = os.environ.get("LLAMA_MODEL_DIR")
tokenizer_path = os.environ.get("TOKENIZER_DIR")
generator = Llama.build(
    Llama_dir=Llama_dir,
    tokenizer_path=tokenizer_path,
    max_seq_len=512,
    max_batch_size=4,
)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)


@app.route("/generate", methods=["POST"])
def generate_response():
    data = request.get_json()
    dialogs = data["dialogs"]
    max_gen_len = data.get("max_gen_len", None) #i am setting default value as None , you can set values like 100,200 etc.
    temperature = data.get("temperature", 0.6)
    top_p = data.get("top_p", 0.9)

    results = generator.chat_completion(
        dialogs,
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )

    formatted_results = []
    for dialog, result in zip(dialogs, results):
        formatted_dialog = [{"role": msg["role"], "content": msg["content"]} for msg in dialog]
        formatted_result = {
            "generation": {
                "role": result["generation"]["role"],
                "content": result["generation"]["content"],
            }
        }
        formatted_results.append({"dialog": formatted_dialog, "result": formatted_result})

    return jsonify(formatted_results)


if __name__ == "__main__":
    app.run(debug=True) #change debug mode if you don't like it
