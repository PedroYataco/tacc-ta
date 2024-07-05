import axios from 'axios';

type ServiceResponse={
    sucess:boolean;
    data?:any;
    message?:string;
}
async function getCuento(title:string=''):Promise<ServiceResponse>{
    try{
      const response = await axios({
        method: 'get',
        url: 'http://localhost:8000'+`/generarCuento/${title}`
      });
      if(!response.data.success){
          return {sucess:false,message:response.data.message};
      }
      return {sucess:true,data:response.data.data};
    }
    catch(err:any){
      throw new Error(err.message);
    }
  }

export {getCuento}