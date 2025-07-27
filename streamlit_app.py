import streamlit as st

# Kamus gugus fungsi
gugus_fungsi_kamus = {
    'COOH': 'Asam Karboksilat',
    'CHO': 'Aldehid',
    'COC': 'Keton',
    'OH': 'Alkohol',
    'NH2': 'Amina',
    'COO': 'Ester'    
}

ikatan = {
    'CHC': 'Alkuna',
    'CH2': 'Alkena',
    'CH':'Alkana'
}

# Kamus nama senyawa lengkap (tanpa strip)
kamus_nama_senyawa = {
    'HCOOCH3':{'iupac':'Metil metanoat','trivial':'Metil format','gambar':'metanoat.png',"golongan":"Ester","rumus_umum":"R-COO-R"},
    'HCOOC2H5': {'iupac': 'Etil metanoat', 'trivial': '','gambar':'etil metanoat.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3COOCH3': {'iupac': 'Metil etanoat', 'trivial': '','gambar':'metil etanoat.jpg', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3COOC2H5': {'iupac': 'Etil etanoat', 'trivial': '','gambar':'etil etanoat.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3CH2COOCH3': {'iupac': 'Metil propanoat', 'trivial': '','gambar':'tdm434bh.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3CH2COOC2H5': {'iupac': 'Etil propanoat', 'trivial': '','gambar':'1a8shj38.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3CH2CH2COOCH3': {'iupac': 'Metil butanoat', 'trivial': '','gambar':'metilbutanoat.png','golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3CH2CH2COOC2H5': {'iupac': 'Etil butanoat', 'trivial': '','gambar':'pltsuutq.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3COOCH2CH2CH3': {'iupac': 'Propanil etanoat', 'trivial': '','gambar':'propanil etanoat.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3COOCH(CH3)2': {'iupac': 'Isopropil etanoat', 'trivial': '','gambar':'0jtr3m8o.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'C6H5CH2COOCH3': {'iupac': 'Benzil etanoat', 'trivial': '','gambar':'benzil etanoat.png', 'golongan': 'Ester', 'rumus_umum': 'R-COO-R'},
    'CH3COOCH(CH2CH3)CH3': {'iupac': 'Oktil etanoat', 'trivial': '','gambar':'oktiletanoat.png','golongan': 'Ester', 'rumus_umum':'R-COO-R'},
    'CH3NH2':{'iupac':'Metilamin','trivial':'','gambar':'metilamin.jpg','golongan':'Amina primer','rumus_umum':'R-NH2'},
    'CH3CH32NH': {'iupac': 'Dimetilamin', 'trivial': '','gambar':'dimetilamin.png','golongan': 'Amina sekunder', 'rumus_umum': 'R2NH'},
    'CH3CH3CH3N': {'iupac': 'Trimetilamin', 'trivial': '','gambar':'trimetilamin.png','golongan': 'Amina tersier', 'rumus_umum': 'R3N'},
    'CH3CH2NH2': {'iupac': 'Etilamin', 'trivial': '','gambar':'etilamin.png', 'golongan': 'Amina primer', 'rumus_umum': 'R-NH2'},
    'C6H5CH2NH2': {'iupac': 'Benzilamin', 'trivial': '','gambar':'benzilamin.png','golongan': 'Amina primer', 'rumus_umum': 'ArCH2NH2'},
    'C6H5NH2': {'iupac': 'Anilin', 'trivial': '','gambar':'anilin (2).png', 'golongan': 'Amina primer aromatik', 'rumus_umum': 'Ar-NH2'},
    'CH3OH': {'iupac': 'Metanol', 'trivial': 'Alkohol metil / spiritus', 'gambar':'metanol.png','golongan': 'Alkohol primer', 'rumus_umum': 'R-OH'},
    'C2H5OH': {'iupac': 'Etanol', 'trivial': 'Alkohol etil / alkohol', 'gambar':'etanol.jpg','golongan': 'Alkohol primer', 'rumus_umum': 'R-OH'},
    'CH3CH2CH2OH': {'iupac': '1-Propanol', 'trivial': 'n-Propanol', 'gambar':'1propanol.jpg','golongan': 'Alkohol primer', 'rumus_umum': 'R-OH'},
    'CH3CHOHCH3': {'iupac': '2-Propanol', 'trivial': 'Isopropanol / alkohol gosok','gambar':'2propanol.png', 'golongan': 'Alkohol sekunder', 'rumus_umum': 'R-OH'},
    'CH3CH2CH2CH2OH': {'iupac': '1-Butanol', 'trivial': 'n-Butanol','gambar':'1-butanol.png', 'golongan': 'Alkohol primer', 'rumus_umum': 'R-OH'},
    'CH3CH2CHOHCH3': {'iupac': '2-Butanol', 'trivial': 'sec-Butanol','gambar':'2 butanol.png', 'golongan': 'Alkohol sekunder', 'rumus_umum': 'R-OH'},
    '(CH3)2CHCH2OH': {'iupac': '2-Metil-1-propanol', 'trivial': 'Isobutanol','gambar':'isobutanol.png', 'golongan': 'Alkohol primer', 'rumus_umum': 'R-OH'},
    '(CH3)3COH': {'iupac': '2-Metil-2-propanol', 'trivial': 't-Butanol','gambar':'tbutanol.png', 'golongan': 'Alkohol tersier', 'rumus_umum': 'R-OH'},
    'C6H5CH2OH': {'iupac': 'Benzil alkohol', 'trivial': 'Benzil alkohol','gambar':'benzilakohol.png','golongan': 'Alkohol primer aromatik', 'rumus_umum': 'Ar-CH2OH'},
    'HOCH2CH2OH': {'iupac': 'Etana-1,2-diol', 'trivial': 'Glikol etilen', 'gambar':'glikoletilen.png','golongan': 'Alkohol diol', 'rumus_umum': 'HO-R-OH'},
    'HOCH2CH(OH)CH2OH': {'iupac': 'Propana-1,2,3-triol', 'trivial': 'Gliserol / gliserin', 'gambar':'gliserol.png','golongan': 'Alkohol triol', 'rumus_umum': 'R-(OH)3'},
    'CH3CH(OH)CH3': {'iupac': 'Propan-2-ol', 'trivial': 'Isopropil alkohol','gambar':'iso propil alkohol.jpg', 'golongan': 'Alkohol sekunder', 'rumus_umum':'R-OH'},
    'CH3COCH3': {'iupac': 'Propanon', 'trivial': 'Aseton', 'gambar':'propanon.png','golongan': 'Keton', 'rumus_umum': 'R-CO-R'},
    'CH3COCH2CH3': {'iupac': 'Butanon', 'trivial': 'Metil etil keton','gambar':'butanon.jpg', 'golongan': 'Keton', 'rumus_umum': 'R-CO-R'},
    'CH3COCH2CH2CH3': {'iupac': '2-Pentanon', 'trivial': 'Metil propil keton','gambar':'2 pentanon.png', 'golongan': 'Keton', 'rumus_umum': 'R-CO-R'},
    'CH3COCH2CH2CH2CH3': {'iupac': '2-Heksanon', 'trivial': 'Metil butil keton','gambar':'2 heksanon.png', 'golongan': 'Keton', 'rumus_umum': 'R-CO-R'},
    'C6H5COCH3': {'iupac': '1-Fenil-etanon', 'trivial': 'Asetofenon','gambar':'1 fenil etanon.png', 'golongan': 'Keton aromatik', 'rumus_umum': 'Ar-CO-R'},
    'C6H5COC6H5': {'iupac': '1,2-Difenil-etanon', 'trivial': 'Benzofenon', 'gambar':'1,2 difeniletanon.png','golongan': 'Keton aromatik', 'rumus_umum':'Ar-CO-Ar'},
    'HCHO': {'iupac': 'Metanal', 'trivial': 'Formaldehida','gambar':'metanal.png', 'golongan': 'Aldehid', 'rumus_umum': 'R-CHO'},
    'CH3CHO': {'iupac': 'Etanal', 'trivial': 'Asetaldehida','gambar':'etanal.png', 'golongan': 'Aldehid', 'rumus_umum': 'R-CHO'},
    'CH3CH2CHO': {'iupac': 'Propanal', 'trivial': 'Propionaldehida','gambar':'as.propanoat.png', 'golongan': 'Aldehid', 'rumus_umum': 'R-CHO'},
    'CH3(CH2)2CHO': {'iupac': 'Butanal', 'trivial': 'Butiraldehida','gambar':'butanal.png', 'golongan': 'Aldehid', 'rumus_umum': 'R-CHO'},
    'CH3(CH2)3CHO': {'iupac': 'Pentanal', 'trivial': 'Valeraldehida','gambar':'pentanal.png', 'golongan': 'Aldehid', 'rumus_umum': 'R-CHO'},
    'C6H5CHO': {'iupac': 'Benzena karbaldehida', 'trivial': 'Benzaldehida','gambar':'benzenakarbaldehida.png', 'golongan': 'Aldehid aromatik', 'rumus_umum':'Ar-CHO'},
    'HCOOH': {'iupac': 'Asam metanoat', 'trivial': 'Asam format','gambar':'as.metanoat.png', 'golongan': 'Asam karboksilat', 'rumus_umum': 'R-COOH'},
    'CH3COOH': {'iupac': 'Asam etanoat', 'trivial': 'Asam asetat','gambar':'as.etanoat.png', 'golongan': 'Asam karboksilat', 'rumus_umum': 'R-COOH'},
    'CH3CH2COOH': {'iupac': 'Asam propanoat', 'trivial': 'Asam propionat','gambar':'as.propanoat.png', 'golongan': 'Asam karboksilat', 'rumus_umum': 'R-COOH'},
    'CH3(CH2)2COOH': {'iupac': 'Asam butanoat', 'trivial': 'Asam butirat','gambar':'as.butanoat.png', 'golongan': 'Asam karboksilat', 'rumus_umum': 'R-COOH'},
    'CH3(CH2)3COOH': {'iupac': 'Asam pentanoat', 'trivial': 'Asam valerianat','gambar':'as.pentanoat.png','golongan': 'Asam karboksilat', 'rumus_umum': 'R-COOH'},
    'C6H5COOH': {'iupac': 'Asam benzoat', 'trivial': 'Asam benzoat','gambar':'as.benzanoat.png', 'golongan': 'Asam karboksilat aromatik', 'rumus_umum':'Ar-COOH'},
    'CH4': {'iupac': 'Metana', 'trivial': '-','gambar':'metana.jpg',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH3': {'iupac': 'Etana', 'trivial': '-','gambar':'etana.jpg',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH3': {'iupac': 'Propana', 'trivial': '-','gambar':'propana.jpg',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH2CH3': {'iupac': 'Butana', 'trivial': '-','gambar':'butana.jpg',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH2CH2CH3': {'iupac': 'Pentana', 'trivial': '-','gambar':'pentana.png',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH2CH2CH2CH3': {'iupac': 'Heksana', 'trivial': '-','gambar':'heksana.png',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH2CH2CH2CH2CH3': {'iupac': 'Heptana', 'trivial': '-','gambar':'heptana.png',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH2CH2CH2CH2CH2CH3': {'iupac': 'Oktana', 'trivial': '-','gambar':'oktana.png',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH2CH2CH2CH2CH2CH2CH3': {'iupac': 'Nonana', 'trivial': '-','gambar':'nonana.png', "golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH3CH2CH2CH2CH2CH2CH2CH2CH2CH3': {'iupac': 'Dekana', 'trivial': '-','gambar':'dekana.png',"golongan":"Alkana","rumus_umum":"CnH2n+2"},
    'CH2CH2': {'iupac': 'Etena', 'trivial': 'Etilena','gambar':'etena.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH3': {'iupac': 'Propena', 'trivial': 'Propilena','gambar':'propena.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH2CH3': {'iupac': 'Butena', 'trivial': '-','gambar':'butenas.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH2CH2CH3': {'iupac': 'Pentena', 'trivial': '-','gambar':'pentena.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH2CH2CH2CH3': {'iupac': 'Heksena', 'trivial': '-','gambar':'heksena.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH2CH2CH2CH2CH3': {'iupac': 'Heptena', 'trivial': '-','gambar':'heptena.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH2CH2CH2CH2CH2CH3': {'iupac': 'Oktena', 'trivial': '-','gambar':'oktena.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH2CH2CH2CH2CH2CH2CH3': {'iupac': 'Nonena', 'trivial': '-','gambar':'nonena.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CH2CHCH2CH2CH2CH2CH2CH2CH2CH3': {'iupac': 'Dekena', 'trivial': '-','gambar':'dekuna.png',"golongan":"Alkena","rumus_umum":"CnH2n"},
    'CHCH': {'iupac': 'Etuna', 'trivial': 'Asetilena','gambar':'etuna (2).png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH3': {'iupac': 'Propuna', 'trivial': '-','gambar':'propuna.png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH2CH3': {'iupac': 'Butuna', 'trivial': '-','gambar':'butuna.png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH2CH2CH3': {'iupac': 'Pentuna', 'trivial': '-','gambar':'pentuna (2).png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH2CH2CH2CH3': {'iupac': 'Heksuna', 'trivial': '-','gambar':'qgzmmmyc.png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH2CH2CH2CH2CH3': {'iupac': 'Heptuna', 'trivial': '-','gambar':'heptuna.png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH2CH2CH2CH2CH2CH3': {'iupac': 'Oktuna', 'trivial': '-','gambar':'oktuna.png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH2CH2CH2CH2CH2CH2CH3': {'iupac': 'Nonuna', 'trivial': '-','gambar':'nonuna.png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
    'CHCCH2CH2CH2CH2CH2CH2CH2CH3': {'iupac': 'Dekuna', 'trivial': '-','gambar':'dekuna.png',"golongan":"Alkuna","rumus_umum":"CnH2n-2"},
}


def tentang():
    st.markdown(
        f"""
        <style>
            .blurimg {{
                background-image: url("https://raw.githubusercontent.com/RIVI44/-PROJEK_LPK_/main/bg2.jpg");
                background-size: cover;
                position: fixed;
                inset: 0;
                filter: blur(4px);
                background-color: rgba(0, 0, 0, 0.8); /* Transparent black overlay */
    
            }}
        </style>
        <div class="blurimg"></div>
        """,
        unsafe_allow_html=True
    )
    st.title("🎯Tentang Website")
    st.markdown(
    f"""
    <style>
        p {{
            font-size: 25px;
            color: #2F3E5C;
            text-align: justify;
            font-family:Quicksand;
        
        }}
    </style>
    <p>
     Website ini dibuat dengan tujuan utama untuk memudahkan pelajar dan mahasiswa dalam memahami serta mengklasifikasikan gugus fungsi dalam senyawa organik. 
    
    Dalam pembelajaran kimia organik, pengenalan struktur senyawa dan pengklasifikasian gugus fungsinya seringkali menjadi tantangan, terutama bagi pemula. Oleh karena itu, aplikasi ini hadir sebagai media interaktif yang dapat membantu pengguna mengidentifikasi berbagai gugus fungsi seperti alkohol, eter, aldehid, keton, asam karboksilat, dan lain-lain secara lebih mudah dan cepat.

    
    Selain itu, aplikasi ini juga dirancang untuk membantu pengguna dalam mengetahui nama senyawa berdasarkan aturan penamaan IUPAC maupun nama trivial. Penamaan senyawa organik merupakan bagian penting dalam komunikasi kimia, dan memahami aturan penamaan dapat meningkatkan pemahaman terhadap struktur serta reaktivitas senyawa tersebut.

    
    Keunggulan dari aplikasi ini adalah adanya fitur input atau visualisasi struktur senyawa, baik secara manual melalui antarmuka interaktif maupun melalui gambar (jika didukung). Dengan fitur ini, pengguna tidak hanya membaca teks, tetapi juga dapat melihat langsung bentuk struktur senyawa yang dimaksud, sehingga proses identifikasi dan penamaan menjadi lebih intuitif dan efisien.

    
    Secara keseluruhan, web ini dibuat sebagai alat bantu belajar yang praktis dan edukatif, yang dapat diakses kapan saja dan di mana saja. Dengan memanfaatkan teknologi digital, aplikasi ini bertujuan untuk mendekatkan konsep kimia organik kepada pengguna secara visual, sistematis, dan menyenangkan.
    </p>
    """,
    unsafe_allow_html=True
    )

def teori():
    st.markdown(
        f"""
        <style>
            .blurimg {{
                background-image: url("https://raw.githubusercontent.com/RIVI44/-PROJEK_LPK_/main/bg2.jpg");
                background-size: cover;
                position: fixed;
                inset: 0;
                filter: blur(4px);
                background-color: rgba(0, 0, 0, 0.8); /* Transparent black overlay */
            }}
        </style>
        <div class="blurimg"></div>
        """,
        unsafe_allow_html=True
    )
    st.title("📚Dasar Teori")
    st.markdown(
    f"""
    <style>
        p {{
            font-size: 18px;
            color: red;
        }}
    </style>
    <p>
    Alkana   
    Alkana disebut juga hidrokarbon parafin (bahasa latin parum affinis afinitas kecil). Penamaan ini didasarkan pada sifat alkana yang sukar bereaksi dengan berbagai pereaksi pada kondisi biasa. Rumus umum alkana dapat ditulis sebagai berikut CH2n+2 sehingga untuk harga n = 1, 2, 3, 4, 5, ... dan seterusnya, rumus molekulnya berturut-turut adalah CH, (metana), C₂H₃ (etana), C₂H₃ (propana), C4H10 (butana), CH12 (pentana).....dan seterusnya. Alkana tergolong zat yang kurang reaktif (sukar bereaksi dengan senyawa lain). Pada temperatur ruang tidak bereaksi dengan asam dan basa kuat, tidak dapat dioksidasikan oleh KMnO, atau K2Cr2O7. Alkana dapat terhalogenasi di bawah pengaruh sinar ultra violet atau pada temperatur 250°C-400°C. •	Makin besar jumlah atom C-nya, makin tinggi titik cair, titik didih, dan berat jenisnya	Alkana yang berwujud gas tidak berbau, yang berwujud cairan memiliki bau yang khas, dan yang berbentuk padatan tidak berbau	Semua alkana praktis tidak larut dalam air, tetapi larut dalam pelarut organik.

    Alkena
    Alkena disebut juga hidrokarbon olefin (olefiant gas gas pembentuk minyak). Penamaan ini merujuk pada kenyataan bahwa suku pertama golongan alkena (etena/etilena) jika direaksikan dengan klor atau brom menghasilkan cairan yang menyerupai minyak. Rumus umum alkena dapat ditulis sebagai berikut C,Han, sehingga untuk harga n = 2, 3, 4, 5, ... dan seterusnya, rumus molekulnya berturut-turut adalah C₂H₄ (etena), C₂H₃ (propena), C₂H₃ (butena), CsHto (pentena),....dan seterusnya. Sifar Fisika: pada temperatur ruang, alkena yang mengandung C₂ sampai Ca berupa gas, Cs sampai C17 berupa cairan, sedangkan untuk C₁ atau lebih berupa padatan. Dan pada sifat kimia Pada temperatur ruang, alkena dapat diadisi oleh Cl₂, Br₂, dan la tanpa katalisator, Bereaksi dengan HCI dan H₂SO₄, dan dapat dioksidasi oleh KMnO, dan K2Cr2O7.

    Alkuna
    Rumus umum alkuna dapat ditulis sebagai berikut C,Hana, sehingga untuk harga n2, 3, 4, 5, ... dan seterusnya, rumus molekulnya berturut-turut adalah C₂H₂ (etuna), C₂H₄ (propuna), CH (butuna), CH (pentuna).....dan seterusnya. Senyawa yang terpenting dalam golongan alkuna adalah etuna (asitilena). Sifat fisika Pada temperatur ruang, alkuna yang mengandung C₂ sampai C, berupa gas, Cs sampai C, berupa cairan, sedangkan untuk Cte atau lebih berupa padatan. Dan sifat kimia alkuna mirip dengan alkena, namun alkuna lebih reaktif dari pada alkena. Pada temperatur ruang, alkuna dapat diadisi oleh Cl2, Br2, dan 12 tanpa katalisator, bereaksi dengan HCI dan H₂SO₄, dan dapat dioksidasi oleh KMnO, dan K₂Cr₂O.
    
    Alkohol
    Alkohol adalah senyawaan organik yang dapat dianggap sebagai turunan dari alkana dengan penggantian satu atau lebih atom H pada alkana oleh gugus hidroksil (-OH). Berdasarkan jumlah gugus -OH yang terdapat dalam tiap molekulnya, alkohol dapat dibedakan:1. Alkohol monohidrat, yaitu alkohol yang mengandung satu gugus hidroksil;2. Alkohol dihidrat, yaitu alkohol yang mengandung dua gugus hidroksil; 3. Alkohol trihidrat, yaitu alkohol yang mengandung tiga gugus hidroksil; 4. Alkohol polihidrat, yaitu alkohol yang mengandung empat atau lebih gugus hidroksil. Berdasarkan atom karbon yang mengikat gugus -OH, maka alkohol di bedakan menjadi:
1. Alkohol primer (1) adalah alkohol yang gugus -OH nya diikat oleh atom C primer (atom C yang berikatan dengan satu atom C yang lain).
2. Alkohol sekunder (2") adalah alkohol yang gugus -OH nya diikat oleh atom C sekunderr (atom C yang berikatan dengan dua atom C yang lain).
3. Alkohol tersier (3) adalah alkohol yang gugus -OH nya diikat oleh atom C tersier (atom C yang berikatan dengan tiga atom C yang lain).

     </p>
    """,
    unsafe_allow_html=True
    )




# Fungsi identifikasi gugus fungsi
def identifikasi_gugus_fungsi(rumus):
    hasil = []
    for gugus, nama in gugus_fungsi_kamus.items():
        if gugus in rumus:
            hasil.append(nama)
    return hasil if hasil else ['Tidak teridentifikasi']

def identifikasi_ikatan(rumus):
    for gugus, nama in ikatan.items():
        if rumus.find(gugus) == 0:
           return nama        
    return "Tidak teridentifikasi"


# Judul
def identifikasi():
    st.markdown(
        f"""
        <style>
           .blurimg {{
                background-image: url("https://raw.githubusercontent.com/RIVI44/-PROJEK_LPK_/main/background.jpg");
                background-size: cover;
                position: fixed;
                inset: 0;
                filter: blur(4px);
                background-color: rgba(0, 0, 0, 0.8); /* Transparent black overlay */
            }} 
        </style>
        <div class="blurimg"></div>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🧪 Identifikasi Gugus Fungsi & Tata Nama Senyawa Hidrokarbon")

    # st.image("https://raw.githubusercontent.com/RIVI44/LPK-KEDUA-/main/WhatsApp%20Image%202025-07-19%20at%2013.17.34_bfbfabba.jpg", use_container_width=True)


    # Pilih mode pencarian
    search_mode = st.radio("Cari berdasarkan:", ("Rumus Senyawa", "Nama Senyawa","Gugus Fungsi"))

    if search_mode == "Rumus Senyawa":
        input_rumus = st.text_input("Masukkan rumus senyawa, contoh: CH3CH2COOH atau CH3-CH2-COOH (ditulis huruf kapital) :")
        if input_rumus:
            rumus = input_rumus.replace("-", "").replace("=", "").replace("≡", "")
            hasil = identifikasi_gugus_fungsi(rumus)
            ikatan = identifikasi_ikatan(rumus)

            nama_iupac = "-"
            nama_trivial = "-"
            golongan = "-"
            rumus_umum = "-"
            gambar = None

            if rumus in kamus_nama_senyawa:
                data = kamus_nama_senyawa[rumus]
                nama_iupac = data['iupac']
                nama_trivial = data['trivial']
                gambar = data.get('gambar', None)
                golongan = data.get('golongan', "-")
                rumus_umum = data.get('rumus_umum', "-")
            else:
                if 'Asam Karboksilat' in hasil:
                    nama_iupac = f"Asam {rumus.lower()}"
                elif 'Aldehid' in hasil:
                    nama_iupac = f"{rumus.lower()} - al"
                elif 'Keton' in hasil:
                    nama_iupac = f"{rumus.lower()} - on"
                elif 'Alkohol' in hasil:
                    nama_iupac = f"{rumus.lower()} - ol"
                elif 'Amina' in hasil:
                    nama_iupac = f"{rumus.lower()} - amina"

            st.markdown("### 🔍 Hasil Identifikasi")
            if gambar:
                st.image(f"https://raw.githubusercontent.com/RIVI44/-PROJEK_LPK_/main/{gambar}", width=250)
            with st.container(border=True):
                st.write(f"*Rumus Diberikan:* {input_rumus}")
                st.write(f"*Rumus Distandarisasi:* {rumus}")
                if rumus_umum != "-":
                    st.write(f"*Rumus Umum:* {rumus_umum}")
                if golongan != "-":
                    st.write(f"*Golongan Senyawa:* {golongan}")
                st.write(f"*Gugus Fungsi Terdeteksi:* {', '.join(hasil)}")
                st.write(f"*Nama IUPAC:* {nama_iupac}")
                st.write(f"*Nama Trivial:* {nama_trivial}")

    else:
        input_nama = st.text_input("Masukkan nama senyawa IUPAC atau trivial, contoh: metana, etana, asam asetat ( ditulis hurruf kecil atau huruf kapital):")
        if input_nama:
            input_nama_lower = input_nama.strip().lower()
            found = None
            for rumus, data in kamus_nama_senyawa.items():
                # Cocokkan dengan nama IUPAC atau trivial
                if data['iupac'].lower() == input_nama_lower or data['trivial'].lower() == input_nama_lower:
                    found = (rumus, data)
                    break
            st.markdown("### 🔍 Hasil Identifikasi")
            if found:
                rumus, data = found
                gambar = data.get('gambar', None)
                if gambar:
                    st.image(f"https://raw.githubusercontent.com/RIVI44/-PROJEK_LPK_/main/{gambar}", width=250)
                with st.container(border=True):
                    st.write(f"*Nama Diberikan:* {input_nama}")
                    st.write(f"*Rumus Senyawa:* {rumus}")
                    st.write(f"*Nama IUPAC:* {data['iupac']}")
                    st.write(f"*Nama Trivial:* {data['trivial']}")
                    st.write(f"*Golongan Senyawa:* {data.get('golongan', '-')}")
                    st.write(f"*Rumus Umum:* {data.get('rumus_umum', '-')}")
            else:
                st.warning("Nama senyawa tidak ditemukan dalam database.")


      
option = st.sidebar.radio(
    "🏡Menu :",
    ("Identifikasi Gugus Fungsi", "Dasar Teori", "Tentang Website")
)

if option == "Identifikasi Gugus Fungsi":
    identifikasi()
elif option == "Dasar Teori":
    teori()
elif option == "Tentang Website":
    tentang()    

 
