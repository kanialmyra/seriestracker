1) Membuat proyek Django baru

Langkah-langkah:
1. Membuat direktori lokal baru bernama seriestracker
2. Membuka command prompt dari dalam direktori tersebut
3. Membuat virtual environment
4. Mengaktifkan virtual environment
5. Meng-install dependencies dari file requirements.txt
6. Membuat proyek Django bernama series_tracker
7. Menambahkan * pada ALLOWED_HOSTS di settings.py dan menyimpan file tersebut
8. Menonaktifkan virtual environment
9. Menjalankan perintah git init
10. Membuat branch main baru
11. Menjalankan perintah git remote add origin https://github.com/kanialmyra/seriestracker.git
12. Menambahkan file .gitignore ke direktori lokal
13. Melakukan add, commit, dan push


2) Membuat aplikasi dengan nama main pada proyek tersebut

Langkah-langkah:
1. Mengaktifkan virtual environment pada command prompt direktori lokal seriestracker
2. Membuat aplikasi Django baru bernama main dengan menjalankan perintah "python manage.py startapp main"


3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main

Langkah-langkah:
1. Membuka file settings.py
2. Menambahkan "main" ke dalam list INSTALLED_APPS
3. Menyimpan pada file settings.py


4) Membuat model pada aplikasi main dengan nama Item

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


5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas

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


6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py

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