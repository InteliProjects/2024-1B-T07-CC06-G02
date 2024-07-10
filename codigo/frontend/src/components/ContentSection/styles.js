import styled from "styled-components";

export const ContentSectionContainer = styled.div`
    width: ${(props) => props.width};
    height: ${(props) => props.height};

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    padding: 15px;
    margin-bottom: 25px;
    margin-top: 10px;

    border-radius: 0.5rem;
    background-color: #fff;

    img {
        height: 95%;
        width: auto;

        border-radius: 0.5rem;
    }

    // exibe h1 quando está processando rotas, por isso 100% width/height
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
