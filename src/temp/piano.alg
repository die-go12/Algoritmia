PianoSweep |:
    <w> "--- Iniciando Barrido de Teclas Blancas (A0 -> C8) ---"
    
    ### 1. Inicializamos en la nota más grave ###
    nota <- A0
    
    ### 2. Iteramos hasta llegar a la más aguda (C8) ###
    while nota <= C8 |:
        
        ### Reproducimos la nota ###
        ### (Tu gramática acepta <:> o (:), ambos funcionan) ###
        <:> nota
        
        ### Imprimimos para ver el progreso en consola ###
        <w> "Tocando nota numero:" nota
        
        ### Avanzamos a la siguiente tecla blanca ###
        nota <- nota + 1
    :|
    
    <w> "--- Barrido Completado ---"
:|
