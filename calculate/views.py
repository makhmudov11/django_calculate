import csv

from django.shortcuts import render

# Create your views here.

def calculator_view(request):

    path = "D:/Viscode_python/6-Django/projects/homework_calculator/calculate"

    if request.method == 'POST':
        try:
            son1 = request.POST.get('son1', "")
            son2 = request.POST.get('son2', "")
            amal = request.POST.get('amal', "")

            son1 = float(son1)
            son2 = float(son2)

            if amal == '+':
                natija = son1 + son2
            elif amal == '-':
                natija = son1 - son2
            elif amal == '*':
                natija = son1 * son2
            elif amal == '/':
                if son2 == 0:
                    natija = "0 ga bo‘lish mumkin emas!"
                else:
                    natija = son1 / son2
            else:
                natija = "Noto‘g‘ri amal tanlandi."
            with open(f"{path}/calculate.his.csv", mode='a+', encoding='UTF-8', newline="") as file:
                writer = csv.writer(file)
                if son1 % 2 == 0 and son2 % 2 == 0 and natija % 2 == 0:
                    writer.writerow([int(son1), amal, int(son2), int(natija)])
                else:
                    writer.writerow([son1, amal, son2, natija])
        except Exception as e:
            natija = f"Xatolik, noto‘g‘ri son kiritildi, {e}"

        return render(request, 'calculator.html', {'natija': natija})
    elif request.method == 'GET':
        with open(f"{path}/calculate.his.csv", mode='r', encoding='UTF-8', newline="") as file:
            reader = list(csv.reader(file))
            data = {
                "rows" : reader
            }
            render(request=request, template_name='calculator.html')
            return render(request=request, template_name='calculate_history.html', context=data)

