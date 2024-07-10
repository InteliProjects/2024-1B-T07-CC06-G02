import { Container } from "./styles";

export default function PageContent({
    children,
    display,
    flexDirection,
    alignItems,
    justifyContent,
}) {
    return (
        <Container
            display={display}
            flexDirection={flexDirection}
            alignItems={alignItems}
            justifyContent={justifyContent}
        >
            {children}
        </Container>
    );
}

PageContent.defaultProps = {
    children: null,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
};
