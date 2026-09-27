

create TABLE usuario{
    idUsuario INT primary key,
    nombreUsuario VARCHAR(100) NOT NULL UNIQUE,
    contrasenaHash varchar (255) NOT NULL,
    esAdmin BOOLEAN DEFAULT FALSE
};

create TABLE departamento{
    idDepart INT primary key,
    nombDepart varchar(100) NOT NULL,
    gerentDepart varchar(100)
};

create TABLE empleado {
    idEmple INT PRIMARY KEY,
    nombEmplea VARCHAR(100) NOT NULL,
    direccEmple varchar(200),
    numEmple varchar(12), /* revisar si se manejara numero como varchar o INT */
    mailEmple varchar(100),
    fchContrato DATE,
    salario INT,
    idDepart INT
    FOREIGN KEY (idDepart) REFERENCES departamento(idDepart)
}



