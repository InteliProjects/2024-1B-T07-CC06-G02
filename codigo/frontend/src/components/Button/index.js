import React from "react";
import { StyledButton } from "./styles";

export default function Button({
    background,
    border,
    children,
    width,
    height,
    onClickFunc,
}) {
    return (
        <StyledButton
            background={background}
            border={border}
            width={width}
            height={height}
            onClick={onClickFunc}
        >
            {children}
        </StyledButton>
    );
}

Button.defaultProps = {
    background: "#006D8F",
    border: "none",
    width: "100%",
    height: "40px",
    onClickFunc: () => {},
};
