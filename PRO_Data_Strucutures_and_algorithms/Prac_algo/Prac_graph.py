def home():
age = request.form["age"]
trestbps = request.form["trestbps"]
chol = request.form["chol"]
oldpeak = request.form["oldpeak"]

gender = request.
from
["gender"]
if (gender == "Male"):
    Male = 1
    Female = 0

elif (gender == "Female"):
    Male = 0
    Female = 1

elif (gbs == ""):
    print("Please Select Gender Or we consider you as Male")
    Male = 1
    Female = 0

# FBS
fbs = request.form["fbs"]
if (fbs == "fbs_True"):
    fbs_True = 1
    fbs_False = 0

    elif (fbs == "fbs_False"):
    fbs_True = 0
    fbs_False = 1

elif (fbs == ""):
    print("Please Select Gender Or we consider True")
    Male = 1
    Female = 0

# SLOPE
slope = request.form("slope")
if (slope == "unsloping"):
    unslopping = 1
    flat = 0
    downsampling = 0
elif (slope == "flat"):
    unslopping = 0
    flat = 1
    downsampling = 0
elif (slope == "downsampling"):
    unslopping = 0
    flat = 0
    downsampling = 1

elif (slope == ""):
    print("Please Select Gender Or we consider downsampling")
    unslopping = 0
    flat = 0
    downsampling = 1

# CP
cp = request.form("cp")
if (cp == "typical_angina"):
    typical_angina = 1
    atyoical_angina = 0
    non_typical_angina = 0
    asymtomatic = 0

elif (cp == "atypical_angina"):
    typical_angina = 0
    atyoical_angina = 1
    non_typical_angina = 0
    asymtomatic = 0

elif (cp == "non_typical_angina"):
    typical_angina = 0
    atyoical_angina = 0
    non_typical_angina = 1
    asymtomatic = 0

elif (cp == "asymtomatic"):
    typical_angina = 0
    atyoical_angina = 0
    non_typical_angina = 0
    asymtomatic = 1

elif (cp == ""):
    print("Please Select Gender Or we consider asymtomatic")
    typical_angina = 0
    atyoical_angina = 0
    non_typical_angina = 0
    asymtomatic = 1

# THAL
thal = request.form("thal")
if (thal == "normal"):
    normal = 1
    fixed_defet = 0
    reversable_defect = 0

elif (thal == "fixed_defet"):
    normal = 0
    fixed_defet = 1
    reversable_defect = 0

elif (thal == "reversable_defect"):
    normal = 0
    fixed_defet = 0
    reversable_defect = 1

elif (thal == ""):
    print("Please Select Gender Or we consider reversable_defect")
    normal = 0
    fixed_defet = 0
    reversable_defect = 1

# CA
ca = request.form("ca")
if (ca == "a"):
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0
elif (ca == "b"):
    a = 0
    b = 1
    c = 0
    d = 0
    e = 0
elif (ca == "c"):
    a = 0
    b = 0
    c = 1
    d = 0
    e = 0
elif (ca == "d"):
    a = 0
    b = 0
    c = 0
    d = 1
    e = 0
elif (ca == "e"):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 1

elif (ca == ""):
    print("Please Select Gender Or we consider 'a'")
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0

# RESTECG
restecg = request.form("restecg")
if (restecg == "res_normal"):
    normal = 1
    st_t = 0
    prob = 0
elif (restecg == "st_t"):
    normal = 0
    st_t = 1
    prob = 0
elif (restecg == "prob"):
    normal = 0
    st_t = 0
    prob = 1
elif (restecg == ""):
    print("Please Select Gender Or we consider Normal")
    normal = 1
    st_t = 0
    prob = 0

arr = np.array([[age,
                 gender, Male, Female,
                 trestbps,
                 chol,
                 fbs, fbs_True, fbs_False,
                 oldpeak,
                 slope, upsloping, flat, downsampling,
                 cp, typical_angina, atypical_angina,
                 non_typical_angina, asymtomatic,
                 thal, normal, fixed_defect, reversable_defect,
                 ca, a, b, c, d, e,
                 restecg, res_normal, st_t, prob]])

pred = model.predict(arr)
return render_template('index.html', data=pred)

if pred == 0:
    res_val = "NO HEART PROBLEM"
else:
    res_val = "HEART PROBLEM"

