from pyscript import document, display

def averagecounter(e):

    document.getElementById("student_info").innerHTML = ""
    document.getElementById("summary").innerHTML = ""
    document.getElementById("output").innerHTML = ""
    
   
    first_name = document.getElementById("First_Name").value
    last_name = document.getElementById("Last_Name").value
    
    SCI = float(document.getElementById("SCI").value)
    MATH = float(document.getElementById("MATH").value)
    ENG = float(document.getElementById("ENG").value)
    FIL = float(document.getElementById("FIL").value)
    ICT = float(document.getElementById("ICT").value)
    PE = float(document.getElementById("PE").value)
    

    unities = {
        "SCI": 5,
        "MATH": 5,
        "ENG": 5,
        "FIL": 3,
        "ICT": 2,
        "PE": 1
    }
    
  
    weighted_sum = (SCI*unities["SCI"] + MATH*unities["MATH"] + ENG*unities["ENG"] +
                    FIL*unities["FIL"] + ICT*unities["ICT"] + PE*unities["PE"])
    
    total_units = sum(unities.values())
    gwa = weighted_sum / total_units
    
   
    summary = f"""
SCI: {SCI:.0f} <br>
MATH: {MATH:.0f} <br>
ENG: {ENG:.0f} <br>
FIL: {FIL:.0f} <br>
ICT: {ICT:.0f} <br>
PE: {PE:.0f} <br>
"""
    
   
    document.getElementById("student_info").innerHTML = f"Name: {first_name} {last_name}"
    document.getElementById("summary").innerHTML = summary
    document.getElementById("output").innerHTML = f"Weighted GWA: {gwa:.2f}"
