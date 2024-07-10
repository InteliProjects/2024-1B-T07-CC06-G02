import styled from "styled-components";

export const Container = styled.div`
    width: 15%;
    height: 100%;

    background-color: #3a6ad6;
`;

export const LogoHolder = styled.div`
    width: 100%;
    aspect-ratio: 1 / 1;

    padding-top: 10%;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;

    background-color: #1f263e;

    img {
        width: 45%;
        aspect-ratio: 1 / 1;
    }

    h1 {
        font-family: "Popins", sans-serif;
        font-size: 1.3rem;
        font-weight: 500;
        color: #ffffff;
    }
`;

export const PageSelection = styled.div`
    width: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
`;

export const PageButton = styled.button`
    width: 100%;
    height: 50px;

    display: flex;
    align-items: center;
    justify-content: flex-start;

    margin-bottom: 2px;

    background-color: #006d8f;
    border: none;
    border-left: 5px solid #50b8e4;

    font-family: "Popins", sans-serif;
    font-size: 1.1rem;
    font-weight: 500;
    color: #ffffff;

    cursor: pointer;

    transition: background-color 0.2s;

    &:hover {
        background-color: #1f263e;
        border: px solid #50b8e4;
        border-left: 5px solid #50b8e4;
    }

    @media (max-width: 768px) {
        .Container {
            width: 25%; 
        }
    
`;
