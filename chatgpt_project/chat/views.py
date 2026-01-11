from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_completion(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

def query_view(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")

        if not prompt:
            return JsonResponse({"response": "Please enter a message."})

        reply = get_completion(prompt)
        return JsonResponse({"response": reply})

    return render(request, "index.html")
