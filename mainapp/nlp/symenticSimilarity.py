from sentence_transformers import SentenceTransformer
import torch

def sementic_similariy(model,sen1,sen2):
    sentences = [sen1, sen2]
    embeddings = model.encode(sentences)
    tens_1 = torch.tensor(embeddings[0])
    tens_2 = torch.tensor(embeddings[1])
    # compute cosine similarity
    cosi = torch.nn.CosineSimilarity(dim=0)
    output = cosi(tens_1, tens_2)
    return output



def filter(key,jd_sen,sen_resume):
  filterd_jd=[]
  filterd_res=[]
  for i in jd_sen:
    for j in key:
      # print(j," ",i)
      if j in i:
        filterd_jd.append(i)
        break
  for i in sen_resume:
    for j in key:
      if j in i:
        filterd_res.append(i)
        break
  fr=" ".join(filterd_res)
  fjd=" ".join(filterd_jd)
  return fr,fjd