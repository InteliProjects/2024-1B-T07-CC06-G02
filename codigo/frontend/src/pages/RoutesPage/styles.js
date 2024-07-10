import styled from "styled-components";

export const DoubleSection = styled.div`
    display: flex;
    justify-content: space-between;
    align-items: flex-start;  

    width: 100%;
    min-height: 70%;  
    max-height: 70%;  
    
`;

export const RoutesHeader = styled.div`
    width: 100%;
    height: 60px;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 10px;

    > div {
        width: 45%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    h1 {
        font-size: 1.3rem;
        font-family: "Poppins", sans-serif;
        color: #209d92;
    }

    button {
        display: flex;
        align-items : center;
        justify-content: center;
        height: 40px;

        padding: 5px 20px;
        border: none;   
        border-radius: 5px;
        background-color: #f1f1f1;

        color: #fff;
        font-size: 0.9rem;
        font-family: "Poppins", sans-serif;
    }

    button:first-child {
        background-color: #209d92;
    }

    button:last-child {
        background-color: #858585;
    }
`;

export const RoutesList = styled.div`
    width: calc(100% + 30px); //overcome the padding
    width: calc(100% + 30px); 
    height: calc(100% - 60px);

    padding-bottom: 30px;

    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;

    overflow-y: scroll;

    position: relative;

    &::-webkit-scrollbar {
        width: 0px;
    }

    > h1 {
        width: 100%;
        height: 100%;

        display: flex;
        align-items: center;
        justify-content: center;

        font-family: "Poppins", sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #000;
    }
`;

export const TableHeader = styled.div`
    display: flex;
    justify-content: space-evenly;

    width: 100%;
    min-height: 50px;

    background-color: #fafbff;

    color: #565b6e;
    font-family: "Poppins", sans-serif;
    font-size: 0.8rem;
    text-align: center;

    border-top: 1px solid #ccc;
    border-bottom: 1px solid #ccc;

    div {
        width: calc(100% / 5);
        display: flex;
        justify-content: center;
        align-items: center;
    }
`;

export const InputFile = styled.div`
    position: relative;
`;

export const FileInput = styled.input`
    font-size: 100px;
    position: absolute;
    left: 0;
    top: 0;
    opacity: 0;
`;

export const Label = styled.label`
    display: block;
    padding: 5px 55px;
    background-color: #209d92;
    color: white;
    border-color: grey;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;

    &:hover {
        background-color: #107d72;
    }
`;

export const TableLine = styled.div`
    display: flex;
    justify-content: space-evenly;

    width: 100%;
    min-height: 50px;

    background-color: #fff;

    color: #565b6e;
    font-family: "Poppins", sans-serif;
    font-size: 0.8rem;
    text-align: center;

    div {
        width: calc(100% / 5);
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    input,
    select {
        width: 80%;
        height: 35px;
        padding: 5px;

        border-radius: 5px;
        border: 1px solid #ccc;

        margin-top: 8px;
        margin-bottom: 8px;
    }

    input:focus,
    select:focus {
        border: 1px solid #ccc;
    }
`;
