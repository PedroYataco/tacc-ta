type ButtonProps = {
  text?: string;
  icon?: any;
  variant?: 'primary' | 'secondary';
  iconSize?: number;
  size?: 'sm' | 'md';
  paddingHorizontal?: string;
  fontSize?: string;
  onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
  disabled?: boolean;
  borderColor?: string;
  textColor?: string;
  className?: string;
};

function Button({
  text,
  icon,
  onClick,
  iconSize = 6,
  size = 'md',
  paddingHorizontal = 'px-7',
  fontSize = 'text-buttonLarge',
  disabled = false,
  borderColor = 'border-primary',
  textColor = 'text-secondary',
  className = '',
  variant = 'primary',
  ...rest
}: ButtonProps) {
  const Icon = icon;
  const isEnabled = !disabled;

  const variantClasses = {
    base: `
      font-bold w-fit ${paddingHorizontal} rounded-lg flex items-center transition-colors duration-150
        gap-2 dark:bg-secondary05 justify-center
      `,
    primary: {
      true: 'bg-secondary text-white hover:bg-secondary04',
      false: 'border-primary opacity-[0.3] border',
    },
    secondary: {
      true: `
        bg-transparent border ${borderColor} text-primary dark:bg-transparent 
        dark:border-white dark:text-white hover:bg-secondary04`,
      false: 'border-primary opacity-[0.3] border',
    },
  };

  const sizeClasses = {
    sm: 'py-1.5',
    md: 'py-3',
  };

  return (
    <button
      type="button"
      disabled={disabled}
      onClick={onClick}
      className={`${className} ${variantClasses.base} ${
        variantClasses[variant][`${isEnabled}`]
      } ${sizeClasses[size]}`}
      {...rest}
    >
      {text && <span className={fontSize}>{text}</span>}
      {icon && <Icon className={`h-${iconSize} w-${iconSize}`} />}
    </button>
  );
}

export default Button;
