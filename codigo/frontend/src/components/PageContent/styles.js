import styled from "styled-components";

export const Container = styled.div`
    width: 100%;
    height: calc(100% - 50px);

    display: ${(props) => props.display};
    flex-direction: ${(props) => props.flexDirection};
    align-items: ${(props) => props.alignItems};
    justify-content: ${(props) => props.justifyContent};

    background-color: #f3f6fe;

    padding: 40px;
    padding-bottom: 0;
`;
