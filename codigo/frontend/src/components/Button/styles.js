// styles.js
import styled from "styled-components";

export const StyledButton = styled.button`
    background: ${(props) => props.background};
    border: ${(props) => props.border};
    width: ${(props) => props.width};
    height: ${(props) => props.height};
    cursor: pointer;

    color: #fff;
    font-family: "Poppins", sans-serif;
    font-size: 1rem;
    font-weight: 500;

    border-radius: 0.5rem;
`;
