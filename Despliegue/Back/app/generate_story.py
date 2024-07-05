import re
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import os

tokenizer = GPT2TokenizerFast.from_pretrained(r'.\app\results')
model = GPT2LMHeadModel.from_pretrained(r'.\app\results')


def capitalize_sentences(text):
    sentences = re.split('(?<=[.!?]) +', text)  # Dividir el texto en oraciones
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    return ' '.join(capitalized_sentences)


# Función para generar texto
def generate_story(prompt, max_length=512, num_return_sequences=1):
    # tokenizer = GPT2TokenizerFast.from_pretrained('./results')
    # model = GPT2LMHeadModel.from_pretrained('./results')

    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(
        inputs['input_ids'],
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=True,  # Para generar texto de manera más creativa
        top_k=50,  # Para limitar el número de palabras a considerar para cada paso
        # Para la estrategia de muestreo de núcleo (nucleus sampling)
        top_p=0.95
    )

    stories = [tokenizer.decode(output, skip_special_tokens=True)
               for output in outputs]
    capitalized_stories = [capitalize_sentences(story) for story in stories]
    return capitalized_stories


# if __name__ == '__main__':
#     prompt = "moatian ronki ipaonike"
#     #relative_path = r'.\results'
#     #absolute_path = os.path.abspath(relative_path)

#     #print("Absolute Path:", absolute_path)
#     #print("Path Exists:", os.path.exists(absolute_path))
#     ##print(os.path.exists(r'.\app\results'))  # Should print True if the directory exists
#     ##print(os.listdir(r'.\results'))  # Should list the files in the directory
#     generated_stories = generate_story(
#         prompt, max_length=300, num_return_sequences=3)

#     for i, story in enumerate(generated_stories):
#         print(f"Cuento {i + 1}:\n{story}\n")
