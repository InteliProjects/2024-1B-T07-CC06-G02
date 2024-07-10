import { Container } from "./styles";

export default function Content({
    children,
    display,
    flexDirection,
    justifyContent,
    alignItems,
}) {
    return (
        <Container
            display={display}
            flexDirection={flexDirection}
            justifyContent={justifyContent}
            alignItems={alignItems}
        >
            {children}
        </Container>
    );
}

Content.defaultProps = {
    children: null,
    display: "flex",
    flexDirection: "column",
    justifyContent: "flex-start",
    alignItems: "center",
};
