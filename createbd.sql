

create TABLE usuario{
    idUsuario INT primary key,
    nombreUsuario VARCHAR(100) NOT NULL UNIQUE,
    contrasenaHash VARCHAR (255) NOT NULL,
    esAdmin BOOLEAN DEFAULT FALSE
};

create TABLE departamento{
    idDepart INT primary key,
    nombDepart VARCHAR(100) NOT NULL,
    gerentDepart VARCHAR(100)
};

create TABLE empleado {
    idEmple INT PRIMARY KEY,
    nombEmplea VARCHAR(100) NOT NULL,
    direccEmple VARCHAR(200),
    numEmple VARCHAR(12), /* revisar si se manejara numero como varchar o INT */
    mailEmple VARCHAR(100),
    fchContrato DATE,
    salario INT,
    idDepart INT,
    FOREIGN KEY (idDepart) REFERENCES departamento(idDepart)
};

create TABLE proyecto {
    idProyecto INT PRIMARY KEY,
    nombProyecto VARCHAR(100) NOT NULL UNIQUE,
    descripProyecto VARCHAR(200),
    fchInicio DATE,
}

create TABLE registroTiempo {
    fchTrabajo DATE,
    hrsTrabajadas INT,
    descripTareas VARCHAR(200)
};

create TABLE asignacion {
    idAsign INT PRIMARY KEY,
    fechaAsignacion DATE
};

