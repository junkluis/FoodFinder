function editarPerfil(){
	var descripcion = document.getElementById("descripcion").value;
	var especialidad = document.getElementById("especialidad").value;
	var ayudantes = document.getElementById("ayudantes");
	document.getElementById("desc-perfil").innerHTML = descripcion;
	document.getElementById("esp-perfil").innerHTML = "Especialidad: " + especialidad;
	if(ayudantes.checked == true){
		document.getElementById("ayu-perfil").innerHTML = "Aceptamos ayudantes";	
	}else{
		document.getElementById("ayu-perfil").innerHTML = "No aceptamos ayudantes" ;	
	}
}