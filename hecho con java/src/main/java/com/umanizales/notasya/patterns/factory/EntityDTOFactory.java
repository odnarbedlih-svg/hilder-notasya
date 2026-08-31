package com.umanizales.notasya.patterns.factory;

import com.umanizales.notasya.dtos.EstudianteDTO;
import com.umanizales.notasya.dtos.ProfesorDTO;

/**
 * Patrón Creacional: Factory Method
 * Problema: Centraliza la instanciación de objetos de transferencia DTO según entidad.
 */
public class EntityDTOFactory {

    public static EstudianteDTO.Create createEstudianteDTO(String nombre, String telefono, String correo) {
        return EstudianteDTO.Create.builder()
                .nombre(nombre)
                .telefono(telefono)
                .correo(correo)
                .build();
    }

    public static ProfesorDTO.Create createProfesorDTO(String nombre, String tipoId, String numId, String especialidad) {
        return ProfesorDTO.Create.builder()
                .nombre(nombre)
                .tipoIdentificacion(tipoId)
                .numeroIdentificacion(numId)
                .especialidad(especialidad)
                .build();
    }
}
