import styled from "styled-components";

export const Container = styled.div`
    width: 100%;
    min-height: calc(100% - 40px);

    display: ${(props) => props.display};
    flex-direction: ${(props) => props.flexDirection};
    justify-content: ${(props) => props.justifyContent};
    align-items: ${(props) => props.alignItems};

    overflow-y: scroll;
    padding-right: 15px;

    &::-webkit-scrollbar {
        width: 10px;
        height: 10px;
        border-radius: 5px;
        cursor: pointer;
        background-color: transparent;
    }

    &::-webkit-scrollbar-thumb {
        background-color: #ccc;
        border-radius: 5px;
    }

    &::-webkit-scrollbar-track {
        background-color: transparent;
    }
`;
