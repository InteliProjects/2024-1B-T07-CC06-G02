import styled from "styled-components";

export const Container = styled.div`
    width: 600px;
    height: 350px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;

    ul {
        width: 400px;
        margin-top: 20px;
    }

    li {
        width: 100%;
        height: 30px;

        margin-bottom: 10px;

        display: flex;
        align-items: center;
        justify-content: center;

        font-family: "Poppins", sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #999;

        background-color: #dee8ea;
        border-radius: 0.5rem;

        text-overflow: ellipsis;
    }
`;

export const Dropzone = styled.div`
    width: 400px;
    height: 250px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;

    border-radius: 0.5rem;
    color: #999;
    background-color: #dee8ea;

    p {
        font-family: "Poppins", sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #686868;
    }
`;

export const AlgorithmSelection = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 20px;

    label {
        font-family: "Poppins", sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #686868;
        margin-bottom: 10px;
    }

    select {
        width: 100%;
        height: 40px;
        border-radius: 0.5rem;
        font-family: "Poppins", sans-serif;
        font-size: 1rem;
        font-weight: 500;
        color: #686868;
        background-color: #dee8ea;
        border: none;
        padding: 0 10px;
    }
`;
