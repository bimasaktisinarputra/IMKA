import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask, jsonify
import datetime

# idp: id pasien
# idrm: id rekam medis suatu pasien

def obat(nama, jenis, exp, pro, kom):
    data = {
        u'Nama': nama,
        u'Jenis': jenis,
        u'Kadaluarsa': exp,
        u'Produsen': pro,
        u'Keterangan': ket,
    }
    return data


def createob(nama,jenis,exp,pro,ket):
    ps_ref=obat(nama,jenis,exp,pro,ket)
    pasien_ref.document().set(ob_ref)

def getdataobat(idp, **par):
    if 'par' in par:
        if par['par'] == 'Nama':
            return obat_ref.document(idp).get().get("Nama")
        elif par['par'] == 'Jenis':
            return obat_ref.document(idp).get().get("Jenis")
        elif par['par'] == 'Kadaluarsa':
            return obat_ref.document(idp).get().get("Kadaluarsa")
        elif par['par'] == 'Produsen':
            return obat_ref.document(idp).get().get("Produsen")
        elif par['par'] == 'Keterangan':
            return obat_ref.document(idp).get().get("Keterangan")
    else:
        return obat_ref.document(idp).get().to_dict()




cred = credentials.Certificate('kunci.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

pasien_ref = db.collection(u'Obat')

docs = pasien_ref.get()

app = Flask(__name__)


@app.route('/')
def hello():
    a=getdatapasien("Bxx6ygvQsIdsQkOp1eVF")
    return jsonify(a)


<<<<<<< HEAD
 #app.run(host='0.0.0.0')
=======
app.run()
>>>>>>> e377cce7c875cd5031ac920001c6db1eaeebd43c
