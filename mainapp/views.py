from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from nlp.pipeline import extract_details
import os
import shutil
from nlp.symenticSimilarity import filter,sementic_similariy
from nlp.ContextSimilirity import get_similarity
from sentence_transformers import SentenceTransformer
import torch
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
from nlp.keywords import keyword

key=set(keyword)


# Create your views here.
def home(request):
    return render(request, 'base.html')


def upload(request):
    context={}

    #for delete media files
    delete_all_files('/Users/gopalgoyal/Desktop/resume parsing/App/uploadApp/media')

    if request.method=="POST":
        uploaded_jd=request.FILES['job_description']
        uploaded_resumes=request.FILES.getlist('resumes')

        fs=FileSystemStorage()
        name=fs.save(uploaded_jd.name,uploaded_jd)
        jd_url=fs.url(name)

        context['jd_url']=[jd_url]
        context['resume_url']=[]
        urls=[]
        ac_urls=[]
        for i in uploaded_resumes:
            
            name=fs.save(i.name,i)
            res_url=fs.url(name)
            res_url=res_url.split("%20")
            
            res_url=" ".join(res_url)
            ac_urls.append(res_url)
            urls.append(os.getcwd()+res_url)
        details,text_data=extract_details(urls)
        # print(details)
        # print(text_data)
        cnt=0
        for i in details:
            context['resume_url'].append((ac_urls[cnt],i['Name'][0],i['email']))
            cnt+=1
        with open(os.getcwd()+jd_url) as f:
            lines = f.readlines()
        jd = " ".join(lines)
        jd = " ".join(jd.split())
        jd_sen=jd.split('.')
        jd_sen
        result=[]
        corpus=[]
        #data in a map
        for link,text in text_data.items():
            sen_resume=text.split("/n")
            filterd_res,filterd_jd=filter(key,jd_sen,sen_resume)
            a=sementic_similariy(model,filterd_jd,filterd_res)
            result.append((a,link))
            
        result.sort()
        n=len(result)
        result=result[n//2:n]
        # result=result[n/2:n-1]
        for i,j in result:
            t= text_data[j].split("\n")
            t=" ".join(t)
            j=j.split("/")
            j="/"+j[len(j)-2]+"/"+j[len(j)-1]
            corpus.append((t,j))

        res=get_similarity(jd,corpus)
        print(res)
        res.sort()
        context['res']=res

    return render(request, 'upload.html',context)


def delete_all_files(path):
    folder = path
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            continue
