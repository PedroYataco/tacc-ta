import re
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained('./results')
model = GPT2LMHeadModel.from_pretrained('./results')


def capitalize_sentences(text):
    sentences = re.split('(?<=[.!?]) +', text)  # Dividir el texto en oraciones
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    return ' '.join(capitalized_sentences)


# Función para generar texto
def generate_story(prompt, max_length=512, num_return_sequences=1):
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


if __name__ == '__main__':
    prompt = "moatian ronki ipaonike"
    generated_stories = generate_story(
        prompt, max_length=300, num_return_sequences=3)

    for i, story in enumerate(generated_stories):
        print(f"Cuento {i + 1}:\n{story}\n")
