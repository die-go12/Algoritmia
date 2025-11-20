### Ejemplo: Main declarado al final CORREGIDO ###

Saludo |:
    <w> "Preparando la orquesta..."
:|

TocarGraves |:
    <w> "Tocando bajos..."
    (:) { C2 E2 G2 }
:|

TocarAgudos |:
    <w> "Tocando melodía..."
    (:) { C5 E5 G5 }
:|

### Main ###
Main |:
    Saludo
    
    ### Esta instruccion <w> rompe la cadena, asi Saludo no se come a TocarGraves ###
    <w> "--- Inicio de sección grave ---"
    TocarGraves
    
    ### Otra ruptura para que TocarGraves no se coma a TocarAgudos ###
    <w> "--- Inicio de sección aguda ---"
    TocarAgudos
    
    <w> "Concierto finalizado."
:|
