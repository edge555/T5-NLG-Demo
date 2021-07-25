import time
from transformers import AutoConfig
from transformers import T5Tokenizer, T5ForConditionalGeneration

config = AutoConfig.from_pretrained('t5-base')
model = T5ForConditionalGeneration.from_pretrained('t5_nlg_demo.bin', return_dict=True,config='t5-base-config.json')

tokenizer = T5Tokenizer.from_pretrained('t5-base')
def generate(text):
    model.eval()
    input_ids = tokenizer.encode("WebNLG:{} ".format(text), return_tensors="pt")
    s = time.time()
    outputs = model.generate(input_ids)
    gen_text = tokenizer.decode(outputs[0]).replace('<pad>', '').replace('</s>', '')
    elapsed = time.time() - s
    print('Generated in {} seconds'.format(str(elapsed)[:4]))
    print(gen_text)

generate('Arthur Morgan | born 22nd june | 1843 | good man | help | people ')
