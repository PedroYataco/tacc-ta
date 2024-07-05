import { useState } from "react";
import { getCuento } from "../services/generador";

type GeneradorHookReturnType =  {
    fetchGeneradorCuentos: (title:string)=>Promise<void>;
    cuentoGenerado: string;    
    isLoading: boolean;
    error: Error | null;
};


function useGenerador(): GeneradorHookReturnType{
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [error, setError] = useState<Error | null>(null);
    const [cuentoGenerado,setCuentoGenerado] = useState<string>("");
    
    const fetchGeneradorCuentos = async (title:string) => {
        setIsLoading(true);
        try {
            const response = await getCuento(title);
            console.log("Cuento",response);
            setCuentoGenerado(response.data);
            //console.log(financeData);
            //return financeList;
            
        } catch (err:any) {
            setError(err);
            setCuentoGenerado("");
            console.error(err);
        //return [];
        } finally {
            setIsLoading(false);
        }
    };
    
    
    return { fetchGeneradorCuentos,cuentoGenerado,isLoading, error };

}


export {useGenerador}