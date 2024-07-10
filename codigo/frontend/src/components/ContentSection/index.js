import { ContentSectionContainer } from "./styles";
/**
 * ContentSection Component
 * 
 * This component renders a content section.
 * 
 * @param {Object} props - Component properties.
 * @param {ReactNode} props.children - Child elements to be rendered inside the content section.
 * @param {string} props.width - Width of the content section. Default is "100%".
 * @param {string} props.height - Height of the content section. Default is "100%".
 * 
 * @returns {JSX.Element} Content section component.
 */
export default function ContentSection({ children, width, height }) {
    return (
        <ContentSectionContainer width={width} height={height}>
            {children}
        </ContentSectionContainer>
    );
}

ContentSection.defaultProps = {
    width: "100%",
    height: "100%",
};
