This is for testing purpose : 
you need to download llamma from their repo and run it and set path in a file named .env
same for tokenizer
install dependancies:
    pip install flask
    pip install llama
    pip install transformers
    pip install python-dotenv
run the app by "python app.py"


input to api should look like this::

        POST /generate HTTP/1.1
        Host: HOST:PORT
        Content-Type: application/json

        {
        "dialogs": [
            [
            {"role": "user", "content": "What is the capital of France?"},
            {"role": "assistant", "content": "The capital of France is Paris."},
            {"role": "user", "content": "Tell me more about Paris."},
            {"role": "assistant", "content": "Paris is known for its rich history and iconic landmarks."},
            {"role": "user", "content": "What are some popular tourist attractions in Paris?"},
            {"role": "assistant", "content": "Some popular attractions in Paris include the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral."}
            ],
            [
            {"role": "user", "content": "What is the recipe of mayonnaise?"}
            ]
        ],
        "max_gen_len": 100,
        "temperature": 0.7,
        "top_p": 0.8
        }




EXTRAS::
Terms:
temperature->
    In the context of language model generation, "temperature" is a hyperparameter that controls the randomness or diversity of the generated text. It affects how "creative" the model's responses are. When generating text using language models, such as Llama 2, the model makes probabilistic choices at each step to predict the next token (word or character) based on the context provided. The higher the temperature, the more diverse and random the generated text will be, as the model is more likely to explore different possibilities.

    Here's how temperature works:
        - Low temperature (e.g., close to 0): The generated text will be more focused and deterministic. The model will tend to produce more plausible and "safe" responses, as it chooses the most likely tokens at each step.

        - High temperature (e.g., around 1): The generated text will be more diverse and creative. The model will be more exploratory and may produce unexpected or "novel" responses, as it assigns higher probabilities to less likely tokens.

    Choosing an appropriate temperature depends on the specific use case:
        - If you want more controlled and safe responses (e.g., in a customer support chatbot), you may use a lower temperature (e.g., 0.6 or 0.7).

        - If you want more varied and creative responses (e.g., in a conversational AI for entertainment), you may use a higher temperature (e.g., 1.0 or higher).

    Experimenting with different temperature values can help fine-tune the language model's output to match the desired level of creativity and coherence for a particular application.
