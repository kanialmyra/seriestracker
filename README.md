## TUGAS 2
### Cara mengimplementasikan checklist
    (1) Membuat proyek Django baru

    Langkah-langkah: 
        1. Membuat direktori lokal baru bernama seriestracker 
        2. Membuka command prompt dari dalam direktori tersebut 
        3. Membuat virtual environment 
        4. Mengaktifkan virtual environment 
        5. Meng-install dependencies dari file requirements.txt 
        6. Membuat proyek Django bernama series_tracker 
        7. Menambahkan \* pada ALLOWED_HOSTS di settings.py dan menyimpan file tersebut 
        8. Menonaktifkan virtual environment 
        9. Menjalankan perintah git init 
        10. Membuat branch main baru 
        11. Menjalankan perintah git remote add origin https://github.com/kanialmyra/seriestracker.git 
        12. Menambahkan file .gitignore ke direktori lokal 
        13. Melakukan add, commit, dan push

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

### Pertanyaan
#### Q1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    Request -> Internet -> Proyek -> urls.py (URL routing ke aplikasi sesuai request) -> views.py (views.py mengambil data dari models.py dan database serta "menempelkan" template web page dari file html terhadap data) -> Respons ditampilkan dalam bentuk web page

#### Q2. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Penggunaan virtual environment bertujuan untuk bisa mengisolasikan masing-masing proyek. Misalnya jika ada beberapa proyek dalam satu device, dan diperlukan update Django di salah satu proyek, maka update Django bisa dilakukan hanya pada proyek tersebut dengan menggunakan virtual environment. Proyek lain tidak akan terdampak oleh update tersebut dan tetap bisa berjalan secara normal.

#### Q3. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    1. Model-View-Template (MVT)
        MVT adalah konsep arsitektur yang diterapkan dalam pengembangan web, khususnya pada framework Django. Konsep arsitektur ini memisahkan komponen-komponen utama dalam pengembangan web, yang terdiri dari komponen Model, View, dan Template, sehingga setiap komponen bisa dikerjakan secara terpisah sebelum akhirnya "disatukan" di akhir. - Model merupakan komponen yang mewakili struktur data dan logika aplikasi, serta menghubungkan aplikasi dengan basis data - View merupakan komponen yang "menyatukan" tampilan antarmuka aplikasi dengan data yang diambil dari Model - Template adalah komponen yang berfungsi untuk mengatur tampilan aplikasi

    2. Model-View-Controller (MVC)
        Pada dasarnya, MVC memiliki konsep yang sama dengan MVC. Perbedaannya hanya terdapat pada penamaannya. Komponen Template pada konsep MVT ekivalen dengan komponen Controller pada konsep MVC. Framework yang menerapkan konsep ini di antaranya Spring, Laravel, dan Yii.

    3. Model View View Model (MVVM)
        MVVM merupakan konsep arsitektur yang biasa diterapkan dalam pengembangan aplikasi Android. Konsep arsitektur ini berfokus untuk memisahkan logika dan tampilan aplikasi. Dalam penerapannya, MVVM memiliki beberapa komponen, yaitu Model, View, dan ViewModel. Komponen Model dan View pada konsep arsitektur ini ekivalen dengan komponen Model dan View pada konsep arsitektur MVC dan MVT. Sementara itu, komponen ViewModel bertugas untuk berinteraksi dengan model di mana data yang ada akan diteruskan ke layer view.



## TUGAS 3
### Cara mengimplementasikan checklist
    (1) Membuat input form untuk menambahkan objek model pada app sebelumnya

    Langkah-langkah: 
        1. Membuat folder templates pada direktori utama 
        2. Membuat file bernama base.html pada direktori tersebut 
        3. Mengisi file tersebut dengan kode berikut:
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
        8. Mengimport redirect, SeriesForm, dan Item file pada views.py
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

### Pertanyaan
#### Q1. Perbedaan form POST dan GET dalam Django

    POST : 
    - Nilai variabel tidak ditampilkan di URL 
    - Lebih aman, sehingga biasanya digunakan 
    - Tidak dibatasi panjang string untuk mengirim data-data penting seperti password 
    - Biasanya untuk input data melalui form

    GET : 
    - Nilai variabel ditampilkan di URL sehingga user dapat dengan mudah memasukkan nilai variabel baru
    - Kurang aman
    - Panjang string dibatasi hingga 2047 karakter
    - Biasanya untuk input data melalui link

#### Q2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

    - HTML digunakan untuk menentukan elemen-elemen pada web seperti teks, gambar, dan lainnya, sehingga fokus utamanya adalah pada representasi visual dan interaktivitas di web. Sementara itu, XML dan JSON digunakan untuk pertukaran data

    - XML, JSON, dan HTML memiliki struktur yang berbeda. XML dan HTML terdiri dari elemen-elemen yang disusun secara hierarkis. Setiap elemen pada XML dan HTML dimulai dengan sebuah tag yang dibuka <tag> dan diakhiri dengan tag yang ditutup </tag>. Sementara itu, data pada JSON dalam format array, yang terdiri dari key-value pairs.

#### Q3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    - Strukturnya sudah sama seperti Java Script, sehingga dapat dengan mudah diproses oleh browser web dan server menggunakan JavaScript.
    - Strukturnya lebih sederhana (menggunakan nama/value pairs), sehingga lebih ringan dan cepat.
    - JSON didukung oleh sebagian besar bahasa pemrograman modern, tidak hanya JavaScript.

> Hasil akses URL Postman: https://drive.google.com/drive/folders/1sUMqDt-U7wJqi23QO7Og2Rx9rkYWvZE1?usp=sharing



## TUGAS 4
### Cara mengimplementasikan checklist
    (1) Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

    Langkah-langkah:
        1. Mengaktifkan virtual environment
        2. Mengimport beberapa hal dengan menambahkan kode berikut:
            from django.contrib.auth.forms import UserCreationForm
            from django.contrib import messages
        3. Menambahkan fungsi berikut ke dalam file views.py
            def register(request):
                form = UserCreationForm()

                if request.method == "POST":
                    form = UserCreationForm(request.POST)
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'Your account has been successfully created!')
                        return redirect('main:login')
                context = {'form':form}
                return render(request, 'register.html', context)
        4. Membuat file baru dengan nama register.html pada main/templates
        5. Mengisi file tersebut dengan kode template berikut:
            {% extends 'base.html' %} 

            {% block meta %}
            <title>Register</title>
            {% endblock meta %} 

            {% block content %}

            <div class="login">
            <h1>Register</h1>

            <form method="POST">
                {% csrf_token %}
                <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar" /></td>
                </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %}
            </div>

            {% endblock content %}
        6. Mengimport fungsi register yang sudah dibuat di file views.py tadi pada main/urls.py
        7. Menambahkan path url berikut ke dalam urlpatterns
            path('register/', register, name='register'),
        8. Mengimport authenticate dan login pada file views.py dengan kode berikut:
            from django.contrib.auth import authenticate, login
        9. Menambahkan fungsi berikut ke dalam views.py
            def login_user(request):
                if request.method == 'POST':
                    username = request.POST.get('username')
                    password = request.POST.get('password')
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('main:show_main')
                    else:
                        messages.info(request, 'Sorry, incorrect username or password. Please try again.')
                context = {}
                return render(request, 'login.html', context)
        10. Membuat file baru dengan nama login.html pada main/templates
        11. Mengisi file tersebut dengan kode template berikut:
            {% extends 'base.html' %}

            {% block meta %}
            <title>Login</title>
            {% endblock meta %} 

            {% block content %}
            <div class="login">
            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                <tr>
                    <td>Username:</td>
                    <td>
                    <input
                        type="text"
                        name="username"
                        placeholder="Username"
                        class="form-control"
                    />
                    </td>
                </tr>

                <tr>
                    <td>Password:</td>
                    <td>
                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        class="form-control"
                    />
                    </td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login" /></td>
                </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %} Don't have an account yet?
            <a href="{% url 'main:register' %}">Register Now</a>
            </div>

            {% endblock content %}
        12. Mengimport fungsi login_user yang sudah dibuat di file views.py tadi pada main/urls.py
        13. Menambahkan path url berikut ke dalam urlpatterns
            path('login/', login_user, name='login'),
        14. Mengimport logout pada file views.py dengan kode berikut:
            from django.contrib.auth import logout
        15. Menambahkan fungsi berikut ke dalam file views.py
            def logout_user(request):
                logout(request)
                return redirect('main:login')
        16. Menambahkan logout button pada file main.html
            <a href="{% url 'main:logout' %}">
                <button>Logout</button>
            </a>
        17. Mengimport fungsi logout_user yang sudah dibuat di file views.py tadi pada main/urls.py
        18. Menambahkan path url berikut ke dalam urlpatterns
            path('logout/', logout_user, name='logout'),
        19. Mengimport login_required pada main/views.py dengan kode berikut:
            from django.contrib.auth.decorators import login_required
        20. Menambahkan kode berikut di atas fungsi show_main:
            @login_required(login_url='/login')

    (2) Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model buku yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    (3) Menghubungkan model Item dengan User.

    Langkah-langkah:
        1. Mengimport User dari django.contrib.auth.models pada main/models.py
        2. Menambahkan baris kode berikut pada model Item pada main/models.py
            user = models.ForeignKey(User, on_delete=models.CASCADE)
        3. Mengubah fungsi create_series pada main/views.py menjadi sebagai berikut:
            form = SeriesForm(request.POST or None) 

            if form.is_valid() and request.method == "POST":
                series = form.save(commit=False)
                series.user = request.user
                series.save()
                return redirect('main:show_main')

            context = {'form': form}
            return render(request, "create_series.html", context)
        4. Mengubah variabel series dan value dari key 'name' pada fungsi show_main pada main/views.py menjadi sebagai berikut:
            def show_main(request):
                books = Book.objects.filter(user=request.user)

                context = {
                    'name': request.user.username, 
                    ...
                }
        5. Menyiapkan migrasi model dengan menjalankan perintah "python manage.py makemigrations"
        6. Mengetik angka 1 ketika saat muncul error, 
        7. Mengetik angka 1 lagi untuk menetapkan user dengan ID 1
        8. Menerapkan migrasi model dengan menjalankan perintah "python manage.py migrate"

    (4) Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    Langkah-langkah:
        1. Mengimport beberapa hal pada views.py dengan kode berikut:
            import datetime
            from django.http import HttpResponseRedirect
            from django.urls import reverse
        2. Memodifikasi kode pada blok if user is not none pada main/views.py menjadi sebagai berikut:
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        3. Menambahkan kode berikut ke dalam dictionary context pada main/views.py:
            'last_login': request.COOKIES['last_login'],
        4. Mengubah fungsi logout_user pada main/views.py menjadi sebagai berikut:
            def logout_user(request):
                logout(request)
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                return response
        5. Menambahkan kode berikut setelah tombol logout pada main/templates/main.html:
            <h5>Sesi terakhir login: {{ last_login }}</h5>

### Pertanyaan
#### Q1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

    UserCreationForm adalah formulir bawaan yang disediakan oleh framework Django untuk memudahkan penggunaan form tanpa harus menulis kode dari awal.

#### Q2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

    Autentikasi adalah proses memverifikasi "siapa" yang mengirimkan request ke server, apakah user tersebut valid dan sudah terdaftar pada database, dan lain sebagainya. Sementara otorisasi adalah proses memverifikasi "apa" saja yang berhak untuk diakses oleh user tersebut. Kedua proses verifikasi tersebut penting untuk dilakukan untuk menghindari berbagai bentuk serangan siber.

#### Q3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

    Cookie adalah sejumlah kecil data yang dikirimkan oleh web server ke browser kemudian dikirimkan lagi ke server jika ada request lain yang datang. Cookies menyimpan data-data yang dapat digunakan untuk autentikasi, tracking user selama beraktivitas di web, dan menyimpan preferensi user yang dapat digunakan untuk iklan dan lain sebagainya. Pada Django, server session disimpan di dalam database dan di-handle secara otomatis pada web server.

#### Q4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    Tidak, terdapat risiko potensial seperti Session Forgery yang memanfaatkan Cookie untuk menginfiltrasi sebuah web. 


## TUGAS 5
### Pertanyaan
#### Q1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    (1) Selector Universal (*):
        Manfaat: Memilih semua elemen di halaman web
        Waktu yang tepat: Ketika ingin menerapkan style secara universal pada seluruh elemen dalam halaman web

    (2) Selector Elemen (Tag Selector):
        Manfaat: Memilih semua elemen HTML dengan tag tertentu, seperti <p>, <div>, <h1>, dan lain-lain
        Waktu yang tepat: Ketika ingin menerapkan style yang sama pada semua elemen dengan tag yang sama

    (3) Selector Kelas (Class Selector):
        Manfaat: Memilih elemen berdasarkan kelas yang ditetapkan untuk elemen tersebut
        Waktu yang tepat: Ketika ingin menerapkan style yang sama pada semua elemen yang memiliki kelas yang sama

    (4) Selector ID (ID Selector):
        Manfaat: Selector ini memilih elemen berdasarkan ID unik yang diberikan kepada elemen tersebut
        Waktu yang tepat: Ketika ingin menerapkan style pada satu elemen saja

    (5) Selector Pseudoelemen (::before, ::after, dll.):
        Manfaat: Memungkinkan untuk membuat elemen virtual dan menerapkan gaya khusus pada bagian-bagian tertentu dari elemen tersebut
        Waktu yang tepat: Ketika ingin menambahkan konten atau style tambahan ke dalam elemen, seperti icon, dekorasi, atau efek animasi

    (6) Selector Pseudo-kelas (:hover, :active, :focus, dll.):
        Manfaat: Memilih elemen berdasarkan keadaan atau interaksi pengguna dengan elemen tersebut
        Waktu yang tepat: Ketika ingin menerapkan style yang berubah saat pengguna melakukan interaksi dengan elemen, seperti hover mouse, klik, atau fokus.

#### Q2. Jelaskan HTML5 Tag yang kamu ketahui
    (1) Tag paragraf (<p>), digunakan untuk menandai paragraf
    (2) Tag teks heading (<h1>, <h2>):, digunakan untuk menandai judul (heading) dan memiliki tingkat kepentingan
    (3) Tag hyperlink ('<a>'), digunakan untuk menampilkan link
    (4) Tag gambar ('<img>'), digunakan untuk menampilkan gambar
    (5) Tag formulir ('<form>), digunakan untuk membuat formulir input
    (6) Tag tabel ('<table>'), digunakan untuk membuat tabel
    (7) Tag kotak teks ('<div>'), digunakan untuk mengelompokkan konten HTML dan menerapkan style CSS atau perilaku JavaScript pada kelompok tersebut 

## TUGAS 6
#### Q1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
**Synchronous Programming**

    - Task dieksekusi satu per satu sesuai urutan
    - Ketika sebuah task dieksekusi, program menunggu hingga task tersebut selesai sebelum melanjutkan ke tugas selanjutnya, sehingga kurang efisien

**Asynchronous Programming**

    - Task dieksekusi secara independen satu sama lain
    - Task dapat dieksekusi secara bersamaan dengan task lainnya
    - Dapat memperbarui hanya bagian-bagian tertentu dari halaman web tanpa harus *reload* seluruh halaman

#### Q2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    Paradigma event-driven programming adalah ketika alur eksekusi program ditentukan oleh terjadinya events (tombol diklik, mengirim request HTTP, dll.) yang terjadi selama program berjalan. Ketika suatu event terjadi, program akan merespons terhadap peristiwa tersebut dengan menjalankan kode yang telah ditentukan sebelumnya untuk menangani event tersebut.

#### Q3. Jelaskan penerapan asynchronous programming pada AJAX.
    Penerapan asynchronous programming pada AJAX melibatkan penggunaan fitur-fitur asynchronous dalam JavaScript untuk mengirim request HTTP ke server dan menangani responsnya tanpa menghentikan eksekusi kode lain di halaman web

#### Q4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
**Fetch API**

    - Sintaksnya lebih modern dan "clean" sehingga lebih mudah digunakan. 
    - Tidak supported di browser lama seperti Internet Explorer (IE)
    - Menawarkan metode yang lebih dasar untuk menangani request HTTP, sehingga respons dapat lebih mendetail dan dapat lebih dikontrol. Namun, konsekuensinya, kita harus menulis lebih banyak kode sendiri untuk menangani hal-hal tertentu karena tidak disediakan secara otomatis.
    
**jQuery**

    - Sintaksnya lebih sederhana dan ringkas
    - Supported baik di browser lama maupun baru
    - Menawarkan fitur-fitur otomatis sehingga dapat dengan cepat menangani request HTTP tanpa harus terlalu banyak menulis kode.

> Secara keseluruhan, pilihan antara Fetch API dan jQuery AJAX bergantung pada preferensi masing-masing. Jika ingin dukungan browser asli dan memiliki lebih banyak kontrol pada alur program, disarankan menggunakan fetch API. Namun, apabila ingin solusi yang lebih cepat dan mudah, disarankan menggunakan jQuery.