import styled from "styled-components";

export const StyledSelect = styled.div`
    width: 100%;
    height: 50px;

    display: flex;
    align-items: center;
    justify-content: center;

    select {
        width: 80%;
        height: 35px;
        padding: 5px;

        border-radius: 5px;
        border: 1px solid #ccc;

        margin-top: 20px;
        margin-bottom: 8px;

        &:focus {
            border: 1px solid #ccc;
        }
    }
`;

export const ComparisonSection = styled.div`
    width: 100%;
    height: calc(100% - 100px);

    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;

    margin-top: 8px;
    margin-bottom: 8px;
    padding-left: 60px;

    font-family: "Poppins", sans-serif;
    text-align: start;

    h1 {
        width: 100%;
        font-size: 2.5rem;
        font-weight: 600;
        color: #000;
    }

    p {
        width: 100%;
        font-size: 1.5rem;
        font-weight: 400;
        color: #000;
    }
`;
