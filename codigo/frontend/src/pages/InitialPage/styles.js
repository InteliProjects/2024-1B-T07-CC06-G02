import styled from "styled-components";

export const Container = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;
`;

export const LogoView = styled.div`
    height: 100%;
    width: 40%;

    background-color: #e2e3e4;

    display: flex;
    flex-direction: column;

    img {
        width: 30%;
        height: auto;
    }

    span {
        color: #3a6ad6;
        font-weight: 700;
    }

    p {
        font-family: "Poppins", sans-serif;
        font-size: 0.8rem;
        font-weight: 300;
    }

    > div {
        height: 50%;

        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
    }
`;

export const InitView = styled.div`
    height: 100%;
    width: 60%;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    h1 {
        font-family: "Poppins", sans-serif;
        font-weight: 500;
        color: #303750;
        font-size: 5rem;
    }

    > div {
        padding-top: 20%;

        width: 100%;
        height: 50%;

        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
`;
