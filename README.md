                                        TUGAS 2

---

Q1. (1) Membuat proyek Django baru
Langkah-langkah: 1. Membuat direktori lokal baru bernama seriestracker 2. Membuka command prompt dari dalam direktori tersebut 3. Membuat virtual environment 4. Mengaktifkan virtual environment 5. Meng-install dependencies dari file requirements.txt 6. Membuat proyek Django bernama series_tracker 7. Menambahkan \* pada ALLOWED_HOSTS di settings.py dan menyimpan file tersebut 8. Menonaktifkan virtual environment 9. Menjalankan perintah git init 10. Membuat branch main baru 11. Menjalankan perintah git remote add origin https://github.com/kanialmyra/seriestracker.git 12. Menambahkan file .gitignore ke direktori lokal 13. Melakukan add, commit, dan push

    (2) Membuat aplikasi dengan nama main pada proyek tersebut
    Langkah-langkah:
        1. Mengaktifkan virtual environment pada command prompt direktori lokal seriestracker
        2. Membuat aplikasi Django baru bernama main dengan menjalankan perintah "python manage.py startapp main"


    (3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main
    Langkah-langkah:
        1. Membuka file settings.py
        2. Menambahkan "main" ke dalam list INSTALLED_APPS
        3. Menyimpan pada file settings.py


    (4) Membuat model pada aplikasi main dengan nama Item
    Langkah-langkah:
        1. Membuka file models.py pada direktori aplikasi main
        2. Mengisi file models.py dengan kode berikut:
            class Item(models.Model):
                name = models.CharField(max_length=255)
                amount = models.IntegerField()
                description = models.TextField()
        3. Menyimpan file models.py
        4. Mengaktifkan virtual environment
        5. Menyiapkan migrasi model dengan menjalankan perintah "python manage.py makemigrations"
        6. Menerapkan migrasi model dengan menjalankan perintah "python manage.py migrate"


    (5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
    Langkah-langkah:
        1. Membuka file views.py pada direktori aplikasi main
        2. Menambahkan kode berikut pada file views.py:
            def show_main(request):
            context = {
                'name': 'Kania Almyra Bilqist',
                'class': 'PBP A'
            }
            return render(request, "main.html", context)
        3. Menyimpan files views.py
        4. Membuat direktori dengan nama templates di dalam direktori aplikasi main
        5. Membuat file main.html di dalam direktori templates
        6. Mengisi file main.html dengan kode berikut:
            <h1>Series Tracker Page</h1>

            <h5>Name:</h5>
            <p>{{ name }}</p>
            <p></p>
            <h5>Class:</h5>
            <p>{{ class }}</p>
        7. Menyimpan file main.html


    (6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
    Langkah-langkah:
        1. Membuat file urls.py di dalam direktori aplikasi main
        2. Mengisi file urls.py dengan kode berikut:
            from django.urls import path
            from main.views import show_main

            app_name = 'main'

            urlpatterns = [
                path('', show_main, name='show_main'),
            ]
        3. Menyimpan file urls.py
        4. Membuka file urls.py di dalam direktori proyek series_tracker
        5. Menambahkan kode berikut pada file urls.py:
            from django.urls import path, include
        6. Menambahkan kode berikut ke dalam list urlpatterns:
            path('', include('main.urls'))
        7. Menyimpan file urls.py
        8. Melakukan add, commit, dan push dari direktori lokal untuk memperbarui repositori GitHub


    (7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
    Langkah-langkah:
        1. Melakukan registrasi di website http://pbp.cs.ui.ac.id
        2. Membuat projek baru
        3. Menjalankan perintah "git remote add pws http://pbp.cs.ui.ac.id/kania.almyra/seriestracker"
        4. Membuat branch baru bernama master dengan menjalankan perintah "git branch -M master"
        5. Melakukan push dengan menjalankan perintah "git push pws master"

Q2. Request -> Internet -> Proyek -> urls.py (URL routing ke aplikasi sesuai request) -> views.py (views.py mengambil data dari models.py dan database serta "menempelkan" template web page dari file html terhadap data) -> Respons ditampilkan dalam bentuk web page

Q3. Penggunaan virtual environment bertujuan untuk bisa mengisolasikan masing-masing proyek. Misalnya jika ada beberapa proyek dalam satu device, dan diperlukan update Django di salah satu proyek, maka update Django bisa dilakukan hanya pada proyek tersebut dengan menggunakan virtual environment. Proyek lain tidak akan terdampak oleh update tersebut dan tetap bisa berjalan secara normal.

Q4. 1. Model-View-Template (MVT)
MVT adalah konsep arsitektur yang diterapkan dalam pengembangan web, khususnya pada framework Django. Konsep arsitektur ini memisahkan komponen-komponen utama dalam pengembangan web, yang terdiri dari komponen Model, View, dan Template, sehingga setiap komponen bisa dikerjakan secara terpisah sebelum akhirnya "disatukan" di akhir. - Model merupakan komponen yang mewakili struktur data dan logika aplikasi, serta menghubungkan aplikasi dengan basis data - View merupakan komponen yang "menyatukan" tampilan antarmuka aplikasi dengan data yang diambil dari Model - Template adalah komponen yang berfungsi untuk mengatur tampilan aplikasi

    2. Model-View-Controller (MVC)
       Pada dasarnya, MVC memiliki konsep yang sama dengan MVC. Perbedaannya hanya terdapat pada penamaannya. Komponen Template pada konsep MVT ekivalen dengan komponen Controller pada konsep MVC. Framework yang menerapkan konsep ini di antaranya Spring, Laravel, dan Yii.

    3. Model View View Model (MVVM)
       MVVM merupakan konsep arsitektur yang biasa diterapkan dalam pengembangan aplikasi Android. Konsep arsitektur ini berfokus untuk memisahkan logika dan tampilan aplikasi. Dalam penerapannya, MVVM memiliki beberapa komponen, yaitu Model, View, dan ViewModel. Komponen Model dan View pada konsep arsitektur ini ekivalen dengan komponen Model dan View pada konsep arsitektur MVC dan MVT. Sementara itu, komponen ViewModel bertugas untuk berinteraksi dengan model di mana data yang ada akan diteruskan ke layer view.



                                               TUGAS 3

---

Q1. (1) Membuat input form untuk menambahkan objek model pada app sebelumnya
Langkah-langkah: 1. Membuat folder templates pada direktori utama 2. Membuat file bernama base.html pada direktori tersebut 3. Mengisi file tersebut dengan kode berikut:
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
{% block meta %} {% endblock meta %}
</head>

            <body>
                {% block content %} {% endblock content %}
            </body>
            </html>
        4. Membuka file settings.py dan melengkapi variabel TEMPLATES menjadi sebagai berikut:
            ...
            TEMPLATES = [
                {
                    ...
                    'DIRS': [BASE_DIR / 'templates'],
                    ...
                }
            ]
            ...
        5. Mengubah isi file main.html menjadi sebagai berikut:
            {% extends 'base.html' %} {% block content %}
            <h1>Book Tracker Page</h1>

            <h5>Name:</h5>
            <p>{{name}}</p>

            <h5>Class:</h5>
            <p>{{class}}</p>
            {% endblock content %}
        6. Membuat file dengan nama forms.py pada direktori main
        7. Menambahkan kode berikut ke dalam file tersebut
            from django.forms import ModelForm
            from main.models import Item

            class SeriesForm(ModelForm):
                class Meta:
                    model = Item
                    fields = ["name", "amount", "description"]
        8. Mengimport redirect, SeriesForm, dan Item file views.py
            from django.shortcuts import render, redirect
            from main.forms import SeriesForm
            from main.models import Item
        9. Membuat fungsi baru pada file views.py dengan menambahkan kode berikut:
            def create_series(request):
                form = SeriesForm(request.POST or None)

                if form.is_valid() and request.method == "POST":
                    form.save()
                    return redirect('main:show_main')

                context = {'form': form}
                return render(request, "create_series.html", context)
        10. Mengubah fungsi show_main pada file views.py menjadi sebagai berikut:
            def show_main(request):
                series = Item.objects.all()

                context = {
                    'name': 'Kania Almyra Bilqist',
                    'class': 'PBP A',
                    'series': series
                }

            return render(request, "main.html", context)
        11. Mengimport fungsi create_series pada file urls.py
        12. Menambahkan path URL ke dalam variabel urlpatterns dengan kode berikut:
            path('create-series', create_series, name='create_series'),
        13. Membuat file dengan nama create_series.html pada direktori templates yang terletak pada direktori main
        14. Mengisi file tersebut dengan kode berikut:
            {% extends 'base.html' %} {% block content %}
            <h1>Add New Series</h1>

            <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Series" />
                </td>
                </tr>
            </table>
            </form>

            {% endblock %}
        15. Menambahkan kode berikut pada file main.html di bawah kode yang sudah ada (masih di dalam {% block content %})
            <table>
            <tr>
                <th>Name</th>
                <th>Amount</th>
                <th>Description</th>

            </tr>

            {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini
            {%endcomment %} {% for serial in series %}
            <tr>
                <td>{{serial.name}}</td>
                <td>{{serial.amount}}</td>
                <td>{{serial.description}}</td>
            </tr>
            {% endfor %}
            </table>

            <br />

            <a href="{% url 'main:create_series' %}">
            <button>Add New Series</button>
            </a>

    (2) Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID
    Langkah-langkah:
        1. Mengimport HttpResponse dan serializers di file views.py:
            from django.http import HttpResponse
            from django.core import serializers
        2. Menambahkan kode berikut pada file views.py untuk melihat objek yang sudah ditambahkan dalam format XML:
            def show_xml(request):
                data = Item.objects.all()
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        3. Menambahkan kode berikut pada file views.py untuk melihat objek yang sudah ditambahkan dalam format JSON:
            def show_json(request):
                data = Item.objects.all()
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        4. Menambahkan kode berikut pada file views.py untuk melihat objek yang sudah ditambahkan dalam format XML by ID:
            def show_xml_by_id(request, id):
                data = Item.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        5. Menambahkan kode berikut pada file views.py untuk melihat objek yang sudah ditambahkan dalam format JSON by ID:
            def show_json_by_id(request, id):
                data = Item.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    (3) Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
    Langkah-langkah
        1. Mengimport fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id (from main.views) di file urls.py
        2. Menambahkan path url berikut ke dalam list urlpatterns untuk mengakses fungsi show_xml
            path('xml/', show_xml, name='show_xml'),
        3. Menambahkan path url berikut ke dalam list urlpatterns untuk mengakses fungsi show_json
            path('xml/', show_xml, name='show_json'),
        4. Menambahkan path url berikut ke dalam list urlpatterns untuk mengakses fungsi show_xml_by_id
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        5. Menambahkan path url berikut ke dalam list urlpatterns untuk mengakses fungsi show_json_by_id
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),

Q2. Perbedaan form POST dan GET dalam Django:
POST : - Nilai variabel tidak ditampilkan di URL - Lebih aman, sehingga biasanya digunakan - Tidak dibatasi panjang string untuk mengirim data-data penting seperti password - Biasanya untuk input data melalui form

    GET  : - Nilai variabel ditampilkan di URL sehingga user dapat dengan mudah memasukkan nilai variabel baru
           - Kurang aman
           - Panjang string dibatasi hingga 2047 karakter
           - Biasanya untuk input data melalui link

Q3. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- HTML digunakan untuk menentukan elemen-elemen pada web seperti teks, gambar, dan lainnya, sehingga fokus utamanya adalah pada representasi visual dan interaktivitas di web. Sementara itu, XML dan JSON digunakan untuk pertukaran data
- XML, JSON, dan HTML memiliki struktur yang berbeda. XML dan HTML terdiri dari elemen-elemen yang disusun secara hierarkis. Setiap elemen pada XML dan HTML dimulai dengan sebuah tag yang dibuka <tag> dan diakhiri dengan tag yang ditutup </tag>. Sementara itu, data pada JSON dalam format array, yang terdiri dari key-value pairs.

Q4. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

- Strukturnya sudah sama seperti Java Script, sehingga dapat dengan mudah diproses oleh browser web dan server menggunakan JavaScript.
- Strukturnya lebih sederhana (menggunakan nama/value pairs), sehingga lebih ringan dan cepat.
- JSON didukung oleh sebagian besar bahasa pemrograman modern, tidak hanya JavaScript.

Hasil akses URL Postman: https://drive.google.com/drive/folders/1sUMqDt-U7wJqi23QO7Og2Rx9rkYWvZE1?usp=sharing